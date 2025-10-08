from fastapi import APIRouter, status, Depends
from src.places.hall_places.schemas import Place, UpdatePlace
from src.places.hall_places.services import PlaceServices
from src.db.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession

place_router = APIRouter(prefix='/places')


place_services = PlaceServices()
@place_router.get("/")
async def getAllPlaces(session: AsyncSession = Depends(get_session)):
    places = await place_services.get_all_places(session)
    return places
@place_router.get("/{place_id}")
async def getPlace(place_id: int, session: AsyncSession = Depends(get_session)):
    place = await place_services.get_place(session, place_id)
    if place:
        return place
    raise status.HTTP_404_NOT_FOUND

@place_router.post("/")
async def addPlace(place: Place, session: AsyncSession = Depends(get_session)):
    await place_services.add_place(session=session, place_type=place.place_type, computer_id=place.computer_id,
                                   headphones_id=place.headphones_id, mouse_id=place.mouse_id, free=place.free,
                                   ready=place.ready)
    return place
@place_router.patch("/{place_id}")
async def updatePlace(place_id: int, update_place: UpdatePlace, session: AsyncSession = Depends(get_session)):
    place = await place_services.get_place(session, place_id)
    if place:
        await place_services.update_place(session=session, place_id=place_id, place_type=update_place.place_type,
            computer_id=update_place.computer_id,headphones_id=update_place.headphones_id,
            mouse_id=update_place.mouse_id, free=update_place.free, ready=update_place.ready)
        return update_place
    raise status.HTTP_404_NOT_FOUND

@place_router.delete("/{place_id}")
async def deletePlace(place_id: int,  session: AsyncSession = Depends(get_session)):
    place = await place_services.get_place(session, place_id)
    if place:
        await place_services.delete_place(session, place_id)
        return {place_id: "deleted"}
    raise status.HTTP_404_NOT_FOUND


