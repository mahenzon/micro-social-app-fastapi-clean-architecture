from typing import Protocol
from uuid import UUID

from social_backend.domain import User


class UserSaver(Protocol):
    async def save(self, user: User) -> None: ...


class UserReader(Protocol):
    async def read_by_uuid(self, uuid: UUID) -> User | None: ...
