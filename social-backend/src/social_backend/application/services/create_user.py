from social_backend.application.interfaces import (
    DBSessionAsync,
    UserSaver,
    UUIDGenerator,
)
from social_backend.application.dto import NewUser
from social_backend.domain import User, UserID


class CreateUserService:
    def __init__(
        self,
        db_session: DBSessionAsync,
        user_saver: UserSaver,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._db_session = db_session
        self._saver = user_saver
        self._uuid_generator = uuid_generator

    async def __call__(self, dto: NewUser) -> UserID:
        uuid = self._uuid_generator()
        book = User(
            id=uuid,
            username=dto.username,
        )
        # мне не нравится, что в saver происходит session.add
        # а тут снаружи мы делаем session.commit
        await self._saver.save(book)
        await self._db_session.commit()
        return uuid
