from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from app.core.db import db_helper, Base
from app.core.config import settings
from app.api_v1 import router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)       # dev time
    yield


app = FastAPI(
    lifespan=lifespan
)

app.include_router(router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.debug)
