from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.site.api_v1.resources.schemas import ResourceCreate
from src.site.core.models import Resource


async def get_resources(session: AsyncSession) -> list[Resource]:
    stmt = select(Resource).order_by(Resource.id)
    result = await session.execute(stmt)
    resources = result.scalars().all()
    return list(resources)


async def create_resource(session: AsyncSession, res: ResourceCreate) -> Resource:
    res = Resource(**res.model_dump())
    session.add(res)
    await session.commit()
    return res
