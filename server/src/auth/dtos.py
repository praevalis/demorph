from enum import Enum

from src.core.dtos import ResponseDto


class TokenTypeEnum(str, Enum):
    """Enum to represent types of authentication tokens."""

    ACCESS = 'access'
    REFRESH = 'refresh'


class TokenDto(ResponseDto):
    sub: str


class AuthDto(ResponseDto):
    access_token: str
    refresh_token: str


class RefreshDto(ResponseDto):
    refresh_token: str
