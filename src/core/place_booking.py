import asyncio
from datetime import datetime
from fastapi import APIRouter
from sqlalchemy.future import select
from src.db.models import Place
from src.db.session import get_session  # ← твой get_session из вопроса

timer = APIRouter()

async def release_expired_places():
    while True:
        session_gen = get_session()
        session = await anext(session_gen)

        try:
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

        finally:
            await session.close()

        await asyncio.sleep(60)

@timer.on_event("startup")
async def startup_event():
    asyncio.create_task(release_expired_places())
