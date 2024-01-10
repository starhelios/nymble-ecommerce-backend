from datetime import datetime

from pydantic import BaseModel

from src.modules.product.schema import ProductResponse


class CreateInventoryDto(BaseModel):
    product_id: str
    stock: int


class InventoryResponse(BaseModel):
    id: str
    product_id: str
    stock: int
    product: ProductResponse | None = None
    created_at: datetime
    updated_at: datetime
