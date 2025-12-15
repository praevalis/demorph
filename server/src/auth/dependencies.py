from uuid import UUID
from fastapi import Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer

from src.auth.dtos import TokenDto
from src.core.config import settings
from src.auth.utils import decode_jwt
from src.auth.services import AuthService
from src.auth.interfaces import UserProvider, LoginUser
from src.core.exceptions.exceptions import Unauthorized

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def get_user_provider() -> UserProvider:
    """Stub method to be overridden."""
    raise NotImplementedError('UserProvider dependency not injected.')


def get_auth_service(
    user_provider: UserProvider = Depends(get_user_provider),
) -> AuthService:
    """
    Dependency injector for auth service.

    Args:
        user_provider: Injected user provider.

    Returns:
        AuthService: Instance of auth service.
    """
    return AuthService(user_provider=user_provider)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_provider: UserProvider = Depends(get_user_provider),
) -> LoginUser:
    """
    Dependency Injector for current user.

    Args:
        token: Bearer token from Authorization header.
        user_provider: Injected user provider.

    Returns:
        LoginUser: Current user.
    """
    payload = decode_jwt(
        token, settings.SECRET_KEY.get_secret_value(), settings.ALGORITHM
    )
    token_data = TokenDto(**payload)

    if not token_data.sub:
        raise Unauthorized('Invalid credentials.')

    try:
        user_uuid = UUID(token_data.sub)
        user = await user_provider.get_user(user_uuid)
    except ValueError:
        raise Unauthorized('Invalid user ID format')

    if user is None:
        raise Unauthorized('User not found')

    return user
