import urllib.parse
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator, computed_field, SecretStr


class Settings(BaseSettings):
    LOG_LEVEL: str
    ENVIRONMENT: Literal['development', 'production'] = 'development'

    ALGORITHM: str
    SECRET_KEY: SecretStr
    REFRESH_TOKEN_EXPIRES_DAYS: int
    ACCESS_TOKEN_EXPIRES_MINUTES: int

    ALLOWED_ORIGINS: str | list[str]

    @field_validator('ALLOWED_ORIGINS', mode='before')
    @classmethod
    def parse_allowed_orgins(cls, v) -> list[str]:
        if isinstance(v, list):
            return v

        elif isinstance(v, str):
            return [origin.strip() for origin in v.split(',') if origin.strip()]

        else:
            raise TypeError(f'Invalid type for ALLOWED_ORIGINS: {type(v)}')

    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_PORT: str

    @computed_field
    @property
    def DB_URL(self) -> str:
        safe_password = urllib.parse.quote_plus(self.DB_PASSWORD.get_secret_value())
        safe_username = urllib.parse.quote_plus(self.DB_USERNAME)

        ssl_param = ''
        if self.ENVIRONMENT != 'development':
            ssl_param = '?ssl=require'

        return (
            f'postgresql+asyncpg://{safe_username}:{safe_password}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}{ssl_param}'
        )

    model_config = SettingsConfigDict(
        env_file=('.env', '.env.local', '.env.production')
    )


settings = Settings()  # type: ignore
