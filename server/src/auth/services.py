from typing import Any
from jwt import PyJWTError
from datetime import timedelta

from src.core.config import settings
from src.auth.interfaces import UserProvider
from src.core.security import verify_password
from src.auth.utils import encode_jwt, decode_jwt
from src.core.exceptions.exceptions import Unauthorized
from src.auth.dtos import AuthDto, TokenTypeEnum, TokenDto


class AuthService:
    """Service for handling authentication."""

    def __init__(self, user_provider: UserProvider) -> None:
        self.user_provider = user_provider

    def _create_access_token(self, data: dict[str, Any]) -> str:
        """
        Creates an access token.

        Args:
            data: Data to be encoded for token.

        Returns:
            str: Created access token.
        """
        return encode_jwt(
            data,
            secret_key=settings.SECRET_KEY.get_secret_value(),
            algorithm=settings.ALGORITHM,
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES_MINUTES),
            token_type=TokenTypeEnum.ACCESS,
        )

    def _create_refresh_token(self, data: dict[str, Any]) -> str:
        """
        Creates a refresh token.

        Args:
            data: Data to be encoded for token.

        Returns:
            str: Created refresh token.
        """
        return encode_jwt(
            data,
            secret_key=settings.SECRET_KEY.get_secret_value(),
            algorithm=settings.ALGORITHM,
            expires_delta=timedelta(minutes=settings.REFRESH_TOKEN_EXPIRES_DAYS),
            token_type=TokenTypeEnum.REFRESH,
        )

    async def authenticate_user(self, username: str, password: str) -> AuthDto:
        """
        Authenticates user using credentials.

        Args:
            username: Identifier used for authentication.
            password: Password to be validated.

        Returns:
            AuthDto: Created access and refresh tokens.

        Raises:
            Unauthorized: When credentials are invalid.
        """
        user = await self.user_provider.get_user_by_username(username)

        if not user:
            raise Unauthorized('Invalid credentials')

        if not verify_password(password, user.password_hash):
            raise Unauthorized('Invalid credentials.')

        return AuthDto(
            access_token=self._create_access_token(
                {'sub': user.id, 'type': TokenTypeEnum.ACCESS}
            ),
            refresh_token=self._create_refresh_token(
                {'sub': user.id, 'type': TokenTypeEnum.REFRESH}
            ),
        )

    async def refresh(self, refresh_token: str) -> AuthDto:
        """
        Verifies the refresh token and creates new access token.

        Args:
            refresh_token: Token to authenticate.

        Returns:
            AuthDto: Refreshed auth tokens.
        """
        token_payload = await self.verify_token(refresh_token, TokenTypeEnum.REFRESH)
        user_id = token_payload.sub

        return AuthDto(
            access_token=self._create_access_token(
                {'sub': user_id, 'type': TokenTypeEnum.ACCESS}
            ),
            refresh_token=self._create_refresh_token(
                {'sub': user_id, 'type': TokenTypeEnum.REFRESH}
            ),
        )

    async def verify_token(
        self, token: str, expected_token_type: TokenTypeEnum
    ) -> TokenDto:
        """
        Verifies given token and returns encoded payload if valid.

        Args:
            token: Token to verify.
            expected_token_type: Type of the token.

        Returns:
            TokenDto: Decoded token data.

        Raises:
            Unauthorized: When the token is invalid.
        """
        try:
            payload = decode_jwt(
                token, settings.SECRET_KEY.get_secret_value(), settings.ALGORITHM
            )

            token_type = payload.get('type')
            if token_type != expected_token_type.value:
                raise Unauthorized('Token type mismatch.')

            user_id = payload.get('sub')
            if not user_id:
                raise Unauthorized('Token payload missing required data.')

            return TokenDto(sub=user_id)

        except (PyJWTError, KeyError):
            raise Unauthorized('Invalid or expired token.')
