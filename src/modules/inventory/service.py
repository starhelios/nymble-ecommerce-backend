from typing import Annotated

from fastapi import Depends

from src.modules.inventory.repository import inventory_repository_dependency
from src.modules.inventory.schema import CreateInventoryDto


class InventoryService:
    def __init__(self, inventory_repository: inventory_repository_dependency):
        self.inventory_repository = inventory_repository

    def get_inventories(self):
        return self.inventory_repository.get_inventories()

    def create_inventory(self, create_inventory_dto: CreateInventoryDto):
        return self.inventory_repository.create_inventory(create_inventory_dto)


inventory_service_dependency = Annotated[InventoryService, Depends(InventoryService)]
