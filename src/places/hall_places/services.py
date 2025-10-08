from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from src.db.models import Place
class PlaceServices:
    async def get_all_places(self, session: AsyncSession):
        places = await session.scalars(select(Place))
        places_list = places.all()
        return places_list

    async def get_place(self, session: AsyncSession, place_id: int):
        place = await session.scalar(select(Place).where(Place.id == place_id))
        return place

    async def add_place(self, session: AsyncSession, place_type, computer_id, headphones_id,  mouse_id, free, ready):
        session.add(Place(place_type=place_type, computer_id=computer_id, headphones_id=headphones_id,
                          mouse_id=mouse_id, free=free, ready=ready))
        await session.commit()

    async def update_place(self, session:AsyncSession, place_id: int, place_type, computer_id, headphones_id,  mouse_id,
                           free, ready):
        place = await session.scalar(select(Place).where(Place.id == place_id))
        place.place_type = place_type
        place.computer_id = computer_id
        place.headphones_id = headphones_id
        place.mouse_id = mouse_id
        place.free = free
        place.ready = ready
        await session.commit()

    async def delete_place(self, session:AsyncSession, place_id: int):
        place = await session.scalar(select(Place).where(Place.id == place_id))
        await session.delete(place)
        await session.commit()