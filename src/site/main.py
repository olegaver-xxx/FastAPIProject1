from contextlib import asynccontextmanager
from core.config import Settings
import uvicorn
from fastapi import FastAPI, Body
from api_v1 import router as router_v1
from core import config
from core.models import db_helper
from src.site.core.config import settings
from src.site.core.models import Base
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

if config.DEBUG:
    if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
else:
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)
