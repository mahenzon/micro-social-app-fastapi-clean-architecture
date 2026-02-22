from social_backend.application.interfaces import (
    DBSessionAsync,
    UserSaver,
)
from social_backend.application.dto import NewUser
from social_backend.domain import User, UserID


class CreateUserInteractor:
    def __init__(
        self,
        db_session: DBSessionAsync,
        user_saver: UserSaver,
    ) -> None:
        self._db_session = db_session
        self._saver = user_saver

    async def __call__(self, dto: NewUser) -> UserID:
        user = User.model_validate(dto)
        user_id = await self._saver.save(user)
        return user_id
