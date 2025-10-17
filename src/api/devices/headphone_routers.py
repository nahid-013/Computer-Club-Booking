from fastapi import APIRouter, Depends, HTTPException
from src.schemas.schemas import Headphone
from src.services.services.headphones_services import HeadphoneServices
from src.db.session import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import List

headphone_router = APIRouter(prefix='/devices/headphones')

headphone_services = HeadphoneServices()
@headphone_router.get("/", response_model=List[Headphone])
async def getAllHeadphone(session: AsyncSession = Depends(get_session)):
    headphones = await headphone_services.get_all_headphones(session)
    return headphones
@headphone_router.get("/{headphone_id}", response_model=Headphone)
async def getHeadphone(headphone_id: int, session: AsyncSession = Depends(get_session)):
    headphone = await headphone_services.get_headphone(session, headphone_id)
    if headphone is not None:
        return headphone
    raise HTTPException(status_code=404, detail="Headphone not found")

@headphone_router.post("/", response_model=List[Headphone])
async def addHeadphone(headphones: List[Headphone], session: AsyncSession = Depends(get_session)):
    for headphone in headphones:
        await headphone_services.add_headphone(session=session, model=headphone.model)
    return headphones
@headphone_router.delete("/{headphone_id}")
async def deleteHeadphone(headphone_id: int, session: AsyncSession = Depends(get_session)):
    headphone = await headphone_services.get_headphone(session, headphone_id)
    if headphone is not None:
        await headphone_services.delete_headphone(session, headphone_id)
        return {"message": f"Headphone {headphone_id} deleted"}
    raise HTTPException(status_code=404, detail="Headphone not found")