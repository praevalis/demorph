from fastapi import Depends
from sqlalchemy import select
from typing import Annotated, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from src.user.models import User
from src.user.schemas import UserDto
from src.auth.schemas import TokenTypeEnum
from src.core.database import sessionmanager
from src.core.exceptions import UnauthorizedException
from src.auth.services import verify_token, oauth2_scheme


async def get_db() -> AsyncGenerator[AsyncSession]:
    """
    Dependency injector async database session.

    Yields:
        AsyncSession: Session instance.
    """
    async with sessionmanager.session() as session:
        yield session
        # Only use flush operation in requests
        # Commit is called after the request is successful
        # This allows 'Unit of work' architecture
        await session.commit()


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(get_db)],
) -> UserDto:
    """
    Dependency Injector for current user.

    Args:
        token: Bearer token from Authorization header.
        session: DB session.

    Returns:
        UserDto: Current user.
    """
    token_data = await verify_token(token, TokenTypeEnum.ACCESS)
    if not token_data:
        raise UnauthorizedException()

    query = select(User).where(User.id == token_data.sub)
    rows = await session.scalars(query)
    user = rows.first()

    if not user:
        raise UnauthorizedException()

    return UserDto.model_validate(user)
