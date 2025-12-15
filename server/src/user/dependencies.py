from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies import get_db
from src.user.services import UserService


def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    """
    Dependency injector for user service.

    Args:
        db: Injected database session.

    Returns:
        UserService: Instance of user service.
    """
    return UserService(db=db)
