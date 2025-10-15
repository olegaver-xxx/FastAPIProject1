from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from src.site.core.models import db_helper
from .schemas import Resource, ResourceCreate

router = APIRouter(tags=["resources"])


@router.get("/", response_model=list[Resource])
async def get_resources(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_resources(session=session)


@router.post("/", response_model=ResourceCreate)
async def create_resource(
    res: ResourceCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_resource(session=session, res=res)
