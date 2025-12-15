from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from src.core.metadata import ApiTags
from src.auth.services import AuthService
from src.auth.dtos import AuthDto, RefreshDto
from src.auth.dependencies import get_auth_service


router = APIRouter(prefix='/auth', tags=[ApiTags.auth])


@router.post(
    '/login',
    status_code=status.HTTP_200_OK,
    response_model=AuthDto,
    response_model_by_alias=True,
)
async def login_user_controller(
    login_data: Annotated[
        OAuth2PasswordRequestForm, Depends()
    ],  # Must be sent through form data by client
    auth_service: AuthService = Depends(get_auth_service),
) -> AuthDto:
    """
    Controller to login user.

    Args:
        login_data: Username and password.
        auth_service: Injected auth service.

    Returns:
        AuthResponseDto: Message, auth tokens and logged user.
    """
    return await auth_service.authenticate_user(
        login_data.username,
        login_data.password,
    )


@router.post(
    '/refresh',
    status_code=status.HTTP_200_OK,
    response_model=AuthDto,
    response_model_by_alias=True,
)
async def refresh_token_controller(
    data: RefreshDto, auth_service: AuthService = Depends(get_auth_service)
) -> AuthDto:
    """
    Controller to refresh access token.

    Args:
        data: Refresh token to be used.
        auth_service: Injected auth service.

    Returns:
        AuthDto: Refreshed tokens.
    """
    return await auth_service.refresh(data.refresh_token)
