import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator, AsyncIterator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

logger = logging.getLogger(__name__)

async_engine = create_async_engine("postgresql+asyncpg://postgres:Test1234@opsguide-db:5432", echo=False)
async_session = async_sessionmaker(bind=async_engine, autoflush=False, future=True)
async_ro_engine = create_async_engine("postgresql+asyncpg://postgres:Test1234@opsguide-db:5432", echo=False)
async_ro_session = async_sessionmaker(bind=async_ro_engine, autoflush=False, future=True)


@asynccontextmanager
async def get_session(ro: bool = False) -> AsyncGenerator[AsyncSession, None]:
    if ro:
        async with async_ro_session() as session:
            async with session.begin():
                try:
                    yield session
                finally:
                    await session.close()
    else:
        async with async_session() as session:
            async with session.begin():
                try:
                    yield session
                finally:
                    await session.close()
