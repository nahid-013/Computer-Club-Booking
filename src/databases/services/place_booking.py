from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from src.databases.models import Place
class BookingPlace:
    async def booking_place(self, time, period, user, place_id, session: AsyncSession):
        place = await session.scalar(select(Place).where(Place.id == place_id))
        place.free = False
        place.ready = True
        await session.commit()
        return place