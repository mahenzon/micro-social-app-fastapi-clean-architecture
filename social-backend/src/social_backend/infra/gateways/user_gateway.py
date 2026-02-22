from sqlalchemy.ext.asyncio import AsyncSession


from social_backend.application.interfaces import UserReader, UserSaver
from social_backend.domain import User, UserID, UserCreate
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
        return User.model_validate(user)

    async def save(self, user_create: UserCreate) -> User:
        user_model = models.User(**user_create.model_dump())
        self._session.add(user_model)
        await self._session.commit()
        return User.model_validate(user_model)
