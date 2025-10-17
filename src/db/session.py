# app/db/session.py
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from src.db.main import async_engine

async_session = async_sessionmaker(async_engine, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
