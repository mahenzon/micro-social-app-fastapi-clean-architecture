from collections.abc import AsyncIterable

from dishka import Provider, Scope, provide, AnyOf
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from social_backend.application import interfaces
from social_backend.application.interactors import (
    GetUserInteractor,
    CreateUserInteractor,
)
from social_backend.config import settings
from social_backend.infra.db import new_session_maker
from social_backend.infra.gateways import UserGateway


class AppProvider(Provider):

    @provide(scope=Scope.APP)
    def get_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return new_session_maker(settings.db)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self,
        session_maker: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[
        AnyOf[
            AsyncSession,
            interfaces.DBSessionAsync,
        ]
    ]:
        async with session_maker() as session:
            yield session

    user_gateway = provide(
        UserGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            interfaces.UserReader,
            interfaces.UserSaver,
        ],
    )

    get_user_interactor = provide(
        GetUserInteractor,
        scope=Scope.REQUEST,
    )
    create_new_user_interactor = provide(
        CreateUserInteractor,
        scope=Scope.REQUEST,
    )
