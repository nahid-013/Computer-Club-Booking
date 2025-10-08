from sqlalchemy import String, Integer, func, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from src.db.config import Config
import datetime
class Base(AsyncAttrs, DeclarativeBase):
    pass

class Place(Base):
    __tablename__ = 'places_table'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    place_type: Mapped[str]
    computer_id: Mapped[int]
    headphones_id: Mapped[int]
    mouse_id: Mapped[int]
    free: Mapped[bool]
    ready: Mapped[bool]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

class Computer(Base):
    __tablename__ = 'computers_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str]
    CPU: Mapped[str]
    RAM: Mapped[str]
    GPU: Mapped[str]

class Headphones(Base):
    __tablename__ = 'headphones_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str]

class Mouse(Base):
    __tablename__ = 'mouse_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str]


async_engine = create_async_engine(Config.database_url, echo=True)

async def create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)