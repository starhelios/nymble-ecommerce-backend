from fastapi import APIRouter

from src.middlewares.auth import auth_dependency
from src.modules.admin.schema import StatsResponse
from src.modules.admin.service import admin_service_dependency

admins = APIRouter(prefix="/api/admin", tags=["admins"])


@admins.get("/stats", response_model=StatsResponse)
def get_stats(admin_service: admin_service_dependency, auth: auth_dependency):
    return admin_service.get_stats()
