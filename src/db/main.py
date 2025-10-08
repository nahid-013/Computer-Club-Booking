import asyncio
from src.db.models import create_db
from sqlalchemy.ext.asyncio import async_sessionmaker
from src.db.models import async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

async def main():
    await create_db()

async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)

    async with async_session() as session:
        yield session

if __name__ == '__main__':
    asyncio.run(main())