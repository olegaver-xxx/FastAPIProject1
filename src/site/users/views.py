from typing import Annotated
from fastapi import APIRouter, Path, Body
from .crud import create_user
from .schemas import CreateUser


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/userlist")
async def get_userlist():
    pass


@router.post("/add_user")
async def add_user(user: CreateUser):
    return create_user(user_in=user)


@router.get("/get_user/{user_id}")
async def get_user_by_id(user_id: int):
    pass
