from social_backend.application.interfaces import UsersReader
from social_backend.domain import User


class GetUsersInteractor:
    def __init__(
        self,
        reader: UsersReader,
    ) -> None:
        self._reader = reader

    async def __call__(self) -> list[User]:
        return await self._reader.read()
