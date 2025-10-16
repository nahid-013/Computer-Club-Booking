from fastapi import APIRouter, status, Depends
from src.places.hall_places.schemas import Computer
from src.databases.services.computer_services import ComputerServices
from src.databases.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import List

computer_router = APIRouter(prefix='/devices/computers')

computer_services = ComputerServices()
@computer_router.get("/", response_model=List[Computer])
async def getAllComputer(session: AsyncSession = Depends(get_session)):
    places = await computer_services.get_all_computers(session)
    return places
@computer_router.get("/{computer_id}", response_model=Computer)
async def getComputer(computer_id: int, session: AsyncSession = Depends(get_session)):
    place = await computer_services.get_computer(session, computer_id)
    if place is not None:
        return place
    raise status.HTTP_404_NOT_FOUND

@computer_router.post("/", response_model=List[Computer])
async def addComputer(computers: List[Computer], session: AsyncSession = Depends(get_session)):
    for computer in computers:
        await computer_services.add_computer(session=session, model=computer.model, CPU=computer.CPU, RAM=computer.RAM,
                                             GPU=computer.GPU, display=computer.display)
    return computers
@computer_router.delete("/{computer_id}")
async def deleteComputer(computer_id: int, session: AsyncSession = Depends(get_session)):
    computer = await computer_services.get_computer(session, computer_id)
    if computer is not None:
        await computer_services.delete_computer(session, computer_id)
        return {computer_id: "deleted"}
    raise status.HTTP_404_NOT_FOUND

