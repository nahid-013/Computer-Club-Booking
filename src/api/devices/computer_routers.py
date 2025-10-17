from fastapi import APIRouter, HTTPException, Depends
from src.schemas.schemas import Computer
from src.services.services.computer_services import ComputerServices
from src.db.session import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import List

computer_router = APIRouter(prefix='/devices/computers')

computer_services = ComputerServices()
@computer_router.get("/", response_model=List[Computer])
async def getAllComputer(session: AsyncSession = Depends(get_session)):
    computers = await computer_services.get_all_computers(session)
    return computers
@computer_router.get("/{computer_id}", response_model=Computer)
async def getComputer(computer_id: int, session: AsyncSession = Depends(get_session)):
    computer = await computer_services.get_computer(session, computer_id)
    if computer is not None:
        return computer
    raise HTTPException(status_code=404, detail="Computer not found")

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
        return {"message": f"Computer {computer_id} deleted"}
    raise HTTPException(status_code=404, detail="Place not found")

