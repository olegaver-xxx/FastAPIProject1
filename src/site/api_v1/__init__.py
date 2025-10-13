from fastapi import APIRouter

from .users.views import router as users_router
from .resources.views import router as resources_router

router = APIRouter()
router.include_router(users_router, prefix="/users")
router.include_router(resources_router, prefix="/resources")
