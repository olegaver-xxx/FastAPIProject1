from fastapi import APIRouter

from .users.views import router as users_router


router_v1 = APIRouter()
router_v1.include_router(users_router, prefix="/users", tags=["Users"])
