from typing import Protocol

from social_backend.domain import User, UserID


class UserSaver(Protocol):
    async def save(self, user: User) -> None: ...


class UserReader(Protocol):
    async def read_by_uuid(self, uuid: UserID) -> User | None: ...


class UsersReader(Protocol):
    async def read(self) -> list[User]: ...
