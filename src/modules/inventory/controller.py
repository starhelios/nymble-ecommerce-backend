from fastapi import APIRouter

from src.modules.inventory.schema import CreateInventoryDto
from src.modules.inventory.schema import InventoryResponse
from src.modules.inventory.service import inventory_service_dependency


inventories = APIRouter(prefix="/api/inventories", tags=["inventories"])


@inventories.get("/", response_model=list[InventoryResponse])
def get_inventories(inventory_service: inventory_service_dependency):
    return inventory_service.get_inventories()


@inventories.post("/", response_model=InventoryResponse)
def create_inventory(
    inventory_service: inventory_service_dependency,
    create_inventory_dto: CreateInventoryDto,
):
    return inventory_service.create_inventory(create_inventory_dto)
