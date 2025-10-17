from fastapi import APIRouter, status, Depends
from src.schemas.schemas import Mouse
from src.services.services.mouse_services import MouseServices
from src.db.session import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import List

mouse_router = APIRouter(prefix='/devices/mouses')

mouse_services = MouseServices()
@mouse_router.get("/", response_model=List[Mouse])
async def getAllMouses(session: AsyncSession = Depends(get_session)):
    mouse = await mouse_services.get_all_mouses(session)
    return mouse
@mouse_router.get("/{mouse_id}", response_model=Mouse)
async def getMouse(mouse_id: int, session: AsyncSession = Depends(get_session)):
    mouse = await mouse_services.get_mouse(session, mouse_id)
    if mouse is not None:
        return mouse
    raise status.HTTP_404_NOT_FOUND

@mouse_router.post("/", response_model=List[Mouse])
async def addMouse(mouses: List[Mouse], session: AsyncSession = Depends(get_session)):
    for mouse in mouses:
        await mouse_services.add_mouse(session=session, model=mouse.model)
    return mouses
@mouse_router.delete("/{mouse_id}")
async def deleteMouse(mouse_id: int, session: AsyncSession = Depends(get_session)):
    mouse = await mouse_services.get_mouse(session, mouse_id)
    if mouse is not None:
        await mouse_services.delete_mouse(session, mouse_id)
        return {mouse_id: "deleted"}
    raise status.HTTP_404_NOT_FOUND