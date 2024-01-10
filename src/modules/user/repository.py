import uuid
from typing import Annotated

from fastapi import Depends
from jose import jwt

from src.modules.user.models import User
from src.modules.user.schema import JwtPayload
from src.modules.user.schema import SignupDto
from src.start.database import db_dependency
from src.start.database import settings


class UserRepository:
    db: db_dependency

    def __init__(self, db: db_dependency) -> None:
        self.db = db

    def get_user_by_id(self, user_id: str):
        return self.db.query(User).filter_by(id=user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter_by(email=email).first()

    def get_users(self):
        return self.db.query(User).all()

    def create_user(self, signup_dto: SignupDto):
        user = User(
            id=str(uuid.uuid4()),
            first_name=signup_dto.first_name,
            last_name=signup_dto.last_name,
            email=signup_dto.email,
            password=signup_dto.password,
        )
        self.db.add(user)
        self.db.commit()
        return user

    def query(self):
        return self.db.query(User)

    def generate_jwt(self, payload: JwtPayload):
        return jwt.encode(
            payload.model_dump(),
            key=settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )


user_repository_dependency = Annotated[UserRepository, Depends(UserRepository)]
