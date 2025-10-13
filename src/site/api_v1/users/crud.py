from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from src.site.api_v1.users.schemas import UserBase, UserCreate
from src.site.core.models import User


async def get_user(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user_by_id(session: AsyncSession, id: int) -> User | None:
    return await session.get(User, id)


async def create_user(session: AsyncSession, user: UserCreate) -> User:
    user = User(**user.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user


async def get_user_by_tg_id(session: AsyncSession, tg_id: int) -> User | None:
    return await session.get(User, tg_id)
