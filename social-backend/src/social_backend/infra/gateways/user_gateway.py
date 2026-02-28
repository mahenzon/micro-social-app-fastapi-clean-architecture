from sqlalchemy.ext.asyncio import AsyncSession

from social_backend.application.interfaces import UserReader, UserSaver
from social_backend.domain import User, UserID
from social_backend.infra import models


class UserGateway(
    UserReader,
    UserSaver,
):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_uuid(
        self,
        uuid: UserID,
    ) -> User | None:
        user = await self._session.get(models.User, uuid)
        if user is None:
            return None
        return User(
            id=user.id,
            username=user.username,
        )

    async def save(self, user: User) -> None:
        user_model = models.User(
            id=user.id,
            username=user.username,
        )
        self._session.add(user_model)
