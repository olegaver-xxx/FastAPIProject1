from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import User, UserCreate
from app.core.db import db_helper

router = APIRouter()



@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_user(session=session)



@router.get("/by-tg-id/{tg_id}/", response_model=User)
async def get_user_by_tg(
    tg_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await crud.get_user_by_tg_id(session=session, tg_id=tg_id)
    print(user)
    return user


@router.get("/{user_id}/", response_model=User)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_user_by_id(session=session, user_id=user_id)



@router.post("/", response_model=User)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(user=user, session=session)
