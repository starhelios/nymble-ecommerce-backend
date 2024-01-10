from datetime import datetime

from pydantic import BaseModel


class CreateProductDto(BaseModel):
    title: str
    description: str
    image: str
    price: float


class ProductResponse(BaseModel):
    id: str
    title: str
    description: str
    image: str
    price: float
    created_at: datetime
    updated_at: datetime


class TopSellingProductResponse(ProductResponse):
    total_sold: int


class ProductSalesResponse(BaseModel):
    product_id: str
    previous_month_sales: float
    current_month_sales: float
