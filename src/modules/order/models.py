from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from src.models.models import CommonBase
from src.modules.product.models import Product
from src.modules.user.models import User


class Order(CommonBase):
    __tablename__ = "orders"
    customer_id = Column(String, ForeignKey("users.id"), nullable=False)
    customer: Mapped["User"] = relationship()


class OrderItem(CommonBase):
    __tablename__ = "order_items"
    order_id = Column(String, ForeignKey("orders.id"), nullable=False)
    order: Mapped["Order"] = relationship()
    product_id = Column(String, ForeignKey("products.id"), nullable=False)
    product: Mapped["Product"] = relationship()
    quantity = Column(Integer)
    price = Column(Float)
