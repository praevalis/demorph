from uuid import UUID
from typing import Any, Protocol

# The purpose of defining protocols is to ensure that `auth` and `user` modules are loosely coupled.
# Ensuring that if the `user` module is changed, it doesn't affects `auth` module.


class LoginUser(Protocol):
    id: UUID
    username: str
    password_hash: str

    def model_dump(self) -> dict[str, Any]: ...


class UserProvider(Protocol):
    async def get_user(self, id: UUID) -> LoginUser: ...

    async def get_user_by_username(self, username: str) -> LoginUser: ...
