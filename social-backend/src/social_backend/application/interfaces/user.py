from typing import Protocol

from social_backend.domain import User, UserID


class UserSaver(Protocol):
    async def save(self, user: User) -> UserID: ...


class UserReader(Protocol):
    async def read_by_uuid(self, uuid: UserID) -> User | None: ...
