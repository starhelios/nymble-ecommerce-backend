from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.models.models import CommonBase
from src.modules.product.models import Product
from src.modules.user.models import User


class Feedback(CommonBase):
    __tablename__ = "feedbacks"
    customer_id = mapped_column(ForeignKey("users.id"))
    customer: Mapped["User"] = relationship()
    product_id = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship()
    rating = Column(Integer)
    comment = Column(String)
