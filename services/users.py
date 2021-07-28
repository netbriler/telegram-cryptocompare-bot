from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db.models import User


async def get_user(session: AsyncSession, id: int,  *args, **props):
    sql = select(User).where(User.id == id)
    query = await session.execute(sql)

    user = query.scalar_one_or_none()

    return user


async def create_user(session: AsyncSession, id: int, name: str, username: str = None, *args, **props):
    new_user = User(id=id, name=name, username=username)

    session.add(new_user)
    await session.commit()

    return new_user


async def get_or_create_user(session: AsyncSession, id: int, name: str, username: str = None, *args, **props):
    user = await get_user(session, id)

    if user:
        return user

    return await create_user(session, id, name, username)

