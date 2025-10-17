from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from src.db.models import Mouse
class MouseServices:
    async def get_all_mouses(self, session: AsyncSession):
        mouses = await session.scalars(select(Mouse))
        mouse_list = mouses.all()
        return mouse_list

    async def get_mouse(self, session: AsyncSession, mouse_id: int):
        mouse = await session.scalar(select(Mouse).where(Mouse.id == mouse_id))
        return mouse

    async def add_mouse(self, session: AsyncSession, model):
        session.add(Mouse(model=model))
        await session.commit()


    async def delete_mouse(self, session:AsyncSession, mouse_id: int):
        mouse = await session.scalar(select(Mouse).where(Mouse.id == mouse_id))
        await session.delete(mouse)
        await session.commit()