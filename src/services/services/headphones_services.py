from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from src.db.models import Headphone
class HeadphoneServices:
    async def get_all_headphones(self, session: AsyncSession):
        headphones = await session.scalars(select(Headphone))
        headphones_list = headphones.all()
        return headphones_list

    async def get_headphone(self, session: AsyncSession, headphone_id: int):
        headphone = await session.scalar(select(Headphone).where(Headphone.id == headphone_id))
        return headphone

    async def add_headphone(self, session: AsyncSession, model):
        session.add(Headphone(model=model))
        await session.commit()


    async def delete_headphone(self, session:AsyncSession, computer_id: int):
        headphone = await session.scalar(select(Headphone).where(Headphone.id == computer_id))
        await session.delete(headphone)
        await session.commit()