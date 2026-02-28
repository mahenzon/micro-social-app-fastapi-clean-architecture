from social_backend.application.interfaces import (
    TransactionManagerAsync,
    UserSaver,
    UUIDGenerator,
)
from social_backend.application.dto import NewUser
from social_backend.domain import User


class CreateUserInteractor:
    def __init__(
        self,
        trx_manager: TransactionManagerAsync,
        user_saver: UserSaver,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._trx_manager = trx_manager
        self._saver = user_saver
        self._generate_uuid = uuid_generator

    async def __call__(self, dto: NewUser) -> User:
        new_user = User(
            id=self._generate_uuid(),
            username=dto.username,
        )
        await self._saver.save(new_user)
        await self._trx_manager.commit()
        return new_user
