import uuid
from typing import Annotated

from fastapi import Depends

from src.modules.inventory.models import Inventory
from src.modules.inventory.schema import CreateInventoryDto
from src.modules.product.models import Product
from src.start.database import db_dependency


class InventoryRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    def get_inventories(self):
        return self.db.query(Inventory).join(Product).all()

    def create_inventory(self, create_inventory_dto: CreateInventoryDto):
        inventory = Inventory(**create_inventory_dto.model_dump(), id=str(uuid.uuid4()))
        self.db.add(inventory)
        self.db.commit()
        self.db.refresh(inventory)
        return inventory


inventory_repository_dependency = Annotated[
    InventoryRepository, Depends(InventoryRepository)
]
