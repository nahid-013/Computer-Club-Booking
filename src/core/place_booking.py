from fastapi import APIRouter
from sqlalchemy.future import select
from src.db.session import async_session
from src.db.models import Place
import asyncio
from datetime import datetime

timer = APIRouter()

async def release_expired_places():
    while True:
        async with async_session() as session:
            now = datetime.utcnow()

            result = await session.scalars(
                select(Place).where(
                    Place.free == False,
                    Place.booked_until <= now
                )
            )
            expired_places = result.all()

            for place in expired_places:
                place.free = True
                place.booked_until = None

            await session.commit()

        await asyncio.sleep(60)

@timer.on_event("startup")
async def startup_event():
    asyncio.create_task(release_expired_places())
