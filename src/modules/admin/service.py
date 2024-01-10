from typing import Annotated

from fastapi import Depends

from src.modules.admin.repository import admin_repository_dependency


class AdminService:
    def __init__(self, admin_repository: admin_repository_dependency):
        self.admin_repository = admin_repository

    def get_stats(self):
        return self.admin_repository.get_stats()


admin_service_dependency = Annotated[AdminService, Depends(AdminService)]
