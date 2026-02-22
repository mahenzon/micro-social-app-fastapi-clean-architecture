from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from social_backend.config.database import DatabaseConfig


def new_session_maker(
    db_config: DatabaseConfig,
) -> async_sessionmaker[AsyncSession]:
    async_engine = create_async_engine(
        url=db_config.async_url,
        pool_size=db_config.sqla.pool_size,
        max_overflow=db_config.sqla.max_overflow,
        connect_args=db_config.sqla.connect_args,
    )
    return async_sessionmaker(
        bind=async_engine,
        autoflush=False,
        expire_on_commit=False,
    )
