from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db.models import User


async def get_user(session: AsyncSession, id: int, *args, **props) -> User:
    sql = select(User).where(User.id == id)
    query = await session.execute(sql)

    user = query.scalar_one_or_none()

    return user


async def create_user(session: AsyncSession, id: int, name: str, username: str = None, language: str = None, *args,
                      **props) -> User:
    new_user = User(id=id, name=name, username=username, language=language)

    session.add(new_user)
    await session.commit()

    return new_user


async def get_or_create_user(session: AsyncSession, id: int, name: str, username: str = None, language: str = None,
                             *args, **props) -> User:
    user = await get_user(session, id)

    if user:
        return user

    return await create_user(session, id, name, username, language)
