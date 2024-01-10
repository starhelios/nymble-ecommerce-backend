from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from src.models.models import CommonBase
from src.modules.product.models import Product


class Inventory(CommonBase):
    __tablename__ = "inventories"
    product_id = Column(String, ForeignKey("products.id"), nullable=False, unique=True)
    product: Mapped["Product"] = relationship()
    stock = Column(Integer)
