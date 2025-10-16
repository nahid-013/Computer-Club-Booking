from sqlalchemy import func, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from src.databases.config import Config
from typing import Optional
import datetime
class Base(AsyncAttrs, DeclarativeBase):
    pass

class Place(Base):
    __tablename__ = 'places_table'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    place_type: Mapped[str]
    computer_id: Mapped[int] = mapped_column(ForeignKey("computers_table.id"), unique=True)
    headphones_id: Mapped[int] = mapped_column(ForeignKey("headphones_table.id"), unique=True, default=1)
    mouse_id: Mapped[int] = mapped_column(ForeignKey("mouses_table.id"), unique=True, default=1)
    free: Mapped[bool]
    ready: Mapped[bool]
    computer: Mapped["Computer"] = relationship(back_populates="place")
    headphone: Mapped["Headphone"] = relationship(back_populates="place")
    mouse: Mapped["Mouse"] = relationship(back_populates="place")
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    booked_until: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

class Computer(Base):
    __tablename__ = 'computers_table'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    model: Mapped[str]
    CPU: Mapped[str]
    RAM: Mapped[str]
    GPU: Mapped[str]
    display: Mapped[str]
    place: Mapped["Place"] = relationship(back_populates="computer")
    # place_id: Mapped[int] = mapped_column(ForeignKey('places_table.id'), unique=True)

class Headphone(Base):
    __tablename__ = 'headphones_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str]
    place: Mapped["Place"] = relationship(back_populates="headphone")
    # place_id: Mapped[int] = mapped_column(ForeignKey('places_table.id'), unique=True)

class Mouse(Base):
    __tablename__ = 'mouses_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str]
    place: Mapped["Place"] = relationship(back_populates="mouse")
    # place_id: Mapped[int] = mapped_column(ForeignKey('places_table.id'), unique=True)


async_engine = create_async_engine(Config.database_url, echo=True)

async def create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)