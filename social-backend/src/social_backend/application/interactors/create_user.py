from social_backend.application.interfaces import (
    DBSessionAsync,
    UserSaver,
)
from social_backend.application.dto import NewUser
from social_backend.domain import User, UserCreate


class CreateUserInteractor:
    def __init__(
        self,
        db_session: DBSessionAsync,
        user_saver: UserSaver,
    ) -> None:
        self._db_session = db_session
        self._saver = user_saver

    async def __call__(self, dto: NewUser) -> User:
        user_create = UserCreate.model_validate(dto)
        new_user = await self._saver.save(user_create)
        return new_user
