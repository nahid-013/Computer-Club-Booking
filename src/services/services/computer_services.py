from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from src.db.models import Computer
class ComputerServices:
    async def get_all_computers(self, session: AsyncSession):
        places = await session.scalars(select(Computer))
        computer_list = places.all()
        return computer_list

    async def get_computer(self, session: AsyncSession, computer_id: int):
        computer = await session.scalar(select(Computer).where(Computer.id == computer_id))
        return computer

    async def add_computer(self, session: AsyncSession, model, CPU, RAM, GPU, display):
        session.add(Computer(model=model, CPU=CPU, RAM=RAM,GPU=GPU, display=display))
        await session.commit()


    async def delete_computer(self, session:AsyncSession, computer_id: int):
        computer = await session.scalar(select(Computer).where(Computer.id == computer_id))
        await session.delete(computer)
        await session.commit()