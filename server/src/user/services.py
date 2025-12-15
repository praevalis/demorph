from uuid import UUID
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from src.user.models import User
from src.core.security import hash_password
from src.core.exceptions.exceptions import NotFound, BadRequest
from src.user.dtos import UserDto, UserCreateDto, UserUpdateDto


class UserService:
    """Service class that handles user management logic."""

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def _get_by_id(self, id: UUID) -> User:
        """
        Private helper to fetch user by ID.

        Args:
            id: ID of the user.

        Returns:
            User: Fetched user.

        Raises:
            NotFound: When user is not found.
        """
        query = select(User).where(User.id == id)
        user = await self.db.scalar(query)

        if not user:
            raise NotFound('User not found.')

        return user

    async def get_user(self, id: UUID) -> UserDto:
        """
        Fetches user by ID.

        Args:
            id: ID of the user to fetch.

        Returns:
            UserDto: Fetched user.
        """
        user = await self._get_by_id(id)
        return UserDto.model_validate(user)

    async def get_user_by_username(self, username: str) -> UserDto:
        """
        Fetches user by username.

        Args:
            username: Username of the user to fetch.

        Returns:
            UserDto: Fetched user.
        """
        query = select(User).where(User.username == username)
        user = await self.db.scalar(query)

        if not user:
            raise NotFound('User not found.')

        return UserDto.model_validate(user)

    async def create_user(self, create_dto: UserCreateDto) -> UserDto:
        """
        Creates new user.

        Args:
            create_dto: Data to create user.

        Returns:
            UserDto: Created user.
        """
        query = select(User).where(
            or_(User.username == create_dto.username, User.email == create_dto.email)
        )
        existing_user = await self.db.scalar(query)

        if existing_user:
            raise BadRequest('Username or email already exists.')

        hashed_pw = hash_password(create_dto.password)

        user = User(
            username=create_dto.username,
            email=create_dto.email,
            first_name=create_dto.first_name.strip(),
            last_name=create_dto.last_name.strip() if create_dto.last_name else None,
            password_hash=hashed_pw,
        )
        self.db.add(user)
        await self.db.flush()
        await self.db.refresh(user)

        return UserDto.model_validate(user)

    async def update_user(self, id: UUID, update_dto: UserUpdateDto) -> UserDto:
        """
        Updates an user.

        Args:
            id: ID of the user to update.
            update_dto: Date to update user.

        Returns:
            UserDto: Updated user.
        """
        user = await self._get_by_id(id)

        if update_dto.password:
            hashed_pw = hash_password(update_dto.password)
            user.password_hash = hashed_pw

        update_dict = update_dto.model_dump(exclude_unset=True, exclude={'password'})
        for key, value in update_dict.items():
            setattr(user, key, value)

        await self.db.flush()
        await self.db.refresh(user)

        return UserDto.model_validate(user)

    async def delete_user(self, id: UUID) -> None:
        """
        Deletes an user.

        Args:
            id: ID of the user to delete.

        Returns:
            None
        """
        user = await self._get_by_id(id)
        await self.db.delete(user)
        await self.db.flush()
