from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String

from src.models.models import CommonBase


class Product(CommonBase):
    __tablename__ = "products"
    title: str = Column(String)
    description: str = Column(String)
    image: str = Column(String)
    price: float = Column(Float)
