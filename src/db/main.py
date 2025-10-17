import asyncio
from src.db.models import Base
from sqlalchemy.ext.asyncio import create_async_engine
from src.core.config import Config

async def main():
    await create_db()

async_engine = create_async_engine(Config.database_url, echo=True)

async def create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(main())