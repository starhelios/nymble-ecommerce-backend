from datetime import datetime

from pydantic import BaseModel


class CreateOrderDto(BaseModel):
    customer_id: str


class CreateOrderItemDto(BaseModel):
    order_id: str
    product_id: str
    quantity: int


class OrderResponse(BaseModel):
    id: str
    customer_id: str
    created_at: datetime
    updated_at: datetime


class OrderItemResponse(BaseModel):
    id: str
    order_id: str
    product_id: str
    quantity: int
    price: float
    created_at: datetime
    updated_at: datetime
