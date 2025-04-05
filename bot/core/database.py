from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import DeclarativeBase

from bot.config import settings


class Base(DeclarativeBase):
    pass


class DatabaseConnection:
    def __init__(self, url: str):
        self.engine = create_async_engine(url=url)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False
        )

    async def async_session(self) -> AsyncSession:
        session = self.session_factory()
        return session


database = DatabaseConnection(url=settings.db_url)
