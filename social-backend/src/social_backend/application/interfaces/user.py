from typing import Protocol

from social_backend.domain import User, UserCreate, UserID


class UserSaver(Protocol):
    async def save(self, user_create: UserCreate) -> User: ...


class UserReader(Protocol):
    async def read_by_uuid(self, uuid: UserID) -> User | None: ...
