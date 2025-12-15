import jwt
from typing import Any
from datetime import datetime, timedelta, UTC
from jwt import ExpiredSignatureError, InvalidTokenError

from src.auth.dtos import TokenTypeEnum
from src.core.exceptions.exceptions import Unauthorized


def encode_jwt(
    payload: dict[str, Any],
    secret_key: str,
    algorithm: str,
    expires_delta: timedelta,
    token_type: TokenTypeEnum,
) -> str:
    """
    Encodes payload into a jwt token.

    Args:
        payload: To be encoded.
        secret_key: Secret key.
        algorithm: Algorithm used for encoding.
        expires_delta: Time when token expires.
        token_type: Type of the token (access, refresh).

    Returns:
        str: Encoded token.
    """
    to_encode = payload.copy()
    to_encode.update({'exp': datetime.now(UTC) + expires_delta, 'type': token_type})

    encoded_token = jwt.encode(payload, secret_key, algorithm)
    return encoded_token


def decode_jwt(token: str, secret_key: str, algorithm: str) -> dict[str, Any]:
    """
    Decodes jwt token into its base payload.

    Args:
        token: To be decoded.
        secret_key: Secret key.
        algorithm: Algorithm used for decoding (should be same as encoding).

    Returns:
        dict[str, Any]: Decoded payload.

    Raises:
        ExpiredSignatureError: When the token has expired.
        InvalidTokenError: When the token is invalid.
    """
    try:
        return jwt.decode(token, key=secret_key, algorithms=[algorithm])

    except ExpiredSignatureError:
        raise Unauthorized('Token expired.')

    except InvalidTokenError:
        raise Unauthorized('Invalid token.')
