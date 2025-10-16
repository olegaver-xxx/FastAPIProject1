from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from .exceptions import UserNotFoundError
from .schemas import UserCreate
from app.api_v1.users.models import User


async def get_user(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    user = await session.get(User, user_id)
    if not user:
        raise UserNotFoundError
    return user


async def create_user(session: AsyncSession, user: UserCreate) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user


async def get_user_by_tg_id(session: AsyncSession, tg_id: int) -> User:
    stm = select(User).where(User.tg_id==tg_id)
    result: Result = await session.execute(stm)
    user: User = result.scalars().first()
    if not user:
        raise UserNotFoundError
    return user
