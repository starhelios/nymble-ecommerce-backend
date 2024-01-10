from sqlalchemy import Column
from sqlalchemy import String

from src.models.models import CommonBase


class User(CommonBase):
    __tablename__ = "users"
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
