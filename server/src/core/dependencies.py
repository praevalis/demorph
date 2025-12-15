from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import sessionmanager


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
