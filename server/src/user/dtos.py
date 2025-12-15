from uuid import UUID
from datetime import datetime
from pydantic import EmailStr, Field

from src.core.dtos import RequestDto, ResponseDto


class UserInternalDto(ResponseDto):
    id: UUID

    username: str
    email: EmailStr
    first_name: str
    last_name: str | None
    password_hash: str

    joined_at: datetime
    updated_at: datetime


class UserDto(ResponseDto):
    id: UUID

    username: str
    email: EmailStr
    first_name: str
    last_name: str | None

    joined_at: datetime
    updated_at: datetime


class UserCreateDto(RequestDto):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str | None = Field(min_length=1, max_length=50)
    password: str = Field(min_length=3, max_length=8, pattern=r'^[A-Za-z\d@$!%*?&]+$')


class UserUpdateDto(RequestDto):
    first_name: str | None = Field(min_length=1, max_length=50, default=None)
    last_name: str | None = Field(min_length=1, max_length=50, default=None)
    password: str | None = Field(
        min_length=3, max_length=8, pattern=r'^[A-Za-z\d@$!%*?&]+$', default=None
    )
