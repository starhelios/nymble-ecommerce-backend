from datetime import datetime

from pydantic import BaseModel
from pydantic import PositiveInt

from src.modules.product.schema import ProductResponse
from src.modules.user.schema import UserResponse


class CreateFeedbackDto(BaseModel):
    customer_id: str
    product_id: str
    rating: PositiveInt
    comment: str


class FeedbackResponse(BaseModel):
    id: str
    rating: PositiveInt
    comment: str
    created_at: datetime
    updated_at: datetime


class FeedbackWithProductResponse(FeedbackResponse):
    product: ProductResponse
    customer: UserResponse
