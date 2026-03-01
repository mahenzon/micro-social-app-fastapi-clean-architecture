import uuid
from collections.abc import AsyncGenerator

from dishka import Provider, Scope, provide, AnyOf
from faststream.rabbit import RabbitBroker
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    AsyncEngine,
)

from social_backend.application.interfaces import (
    TransactionManagerAsync,
    UserSaver,
    UserReader,
    UsersReader,
    UUIDGenerator,
)
from social_backend.application.interactors import (
    GetUserInteractor,
    GetUsersInteractor,
    CreateUserInteractor,
)
from social_backend.config import settings
from social_backend.infra.db import new_session_maker, new_engine
from social_backend.infra.gateways import UserGateway


class AppProvider(Provider):

    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> UUIDGenerator:
        return uuid.uuid7

    @provide(scope=Scope.APP)
    async def get_engine(self) -> AsyncGenerator[AsyncEngine]:
        engine = new_engine(settings.db)
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    def get_session_maker(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return new_session_maker(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self,
        session_maker: async_sessionmaker[AsyncSession],
    ) -> AsyncGenerator[
        AnyOf[
            AsyncSession,
            TransactionManagerAsync,
        ]
    ]:
        async with session_maker() as session:
            yield session

    user_gateway = provide(
        UserGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            UserReader,
            UserSaver,
            UsersReader,
        ],
    )

    get_user_interactor = provide(
        GetUserInteractor,
        scope=Scope.REQUEST,
    )
    get_users_interactor = provide(
        GetUsersInteractor,
        scope=Scope.REQUEST,
    )
    create_new_user_interactor = provide(
        CreateUserInteractor,
        scope=Scope.REQUEST,
    )
