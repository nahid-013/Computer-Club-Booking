from fastapi import APIRouter, status, Depends
from src.schemas.schemas import Place, UpdatePlace
from src.services.services.place_services import PlaceServices
from src.db.session import get_session
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import List

place_router = APIRouter(prefix='/places')

place_services = PlaceServices()
@place_router.get("/", response_model=List[Place])
async def getAllPlaces(session: AsyncSession = Depends(get_session)):
    places = await place_services.get_all_places(session)
    return places
@place_router.get("/{place_id}", response_model=Place)
async def getPlace(place_id: int, session: AsyncSession = Depends(get_session)):
    place = await place_services.get_place(session, place_id)
    if place is not None:
        return place
    raise status.HTTP_404_NOT_FOUND

@place_router.post("/", response_model=list[Place])
async def addPlace(places: List[Place], session: AsyncSession = Depends(get_session)):
    for place in places:
        await place_services.add_place(session=session, place_type=place.place_type, computer_id=place.computer_id,
                                   headphones_id=place.headphones_id, mouse_id=place.mouse_id, free=place.free,
                                   ready=place.ready)
    return places
@place_router.patch("/{place_id}", response_model=UpdatePlace)
async def updatePlace(place_id: int, update_place: UpdatePlace, session: AsyncSession = Depends(get_session)):
    place = await place_services.get_place(session, place_id)
    if place is not None:
        await place_services.update_place(session=session, place_id=place_id, place_type=update_place.place_type,
            computer_id=update_place.computer_id,headphones_id=update_place.headphones_id,
            mouse_id=update_place.mouse_id, free=update_place.free, ready=update_place.ready)
        return update_place
    raise status.HTTP_404_NOT_FOUND

@place_router.delete("/{place_id}")
async def deletePlace(place_id: int, session: AsyncSession = Depends(get_session)):
    place = await place_services.get_place(session, place_id)
    if place is not None:
        await place_services.delete_place(session, place_id)
        return {place_id: "deleted"}
    raise status.HTTP_404_NOT_FOUND


@place_router.post("/book_place/{place_id}")
async def book_place(place_id: int, session: AsyncSession = Depends(get_session)):
    place = await place_services.get_place(session, place_id)

    if not place:
        raise status.HTTP_404_NOT_FOUND
    if not place.free:
        print('not free')
        raise status.HTTP_404_NOT_FOUND

    place.free = False
    place.booked_until = datetime.utcnow() + timedelta(minutes=1)

    await session.commit()
    return {"message": f"Place {place_id} booked for 2 hours"}


