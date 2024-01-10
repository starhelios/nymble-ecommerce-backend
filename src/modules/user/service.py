from typing import Annotated

import bcrypt
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from src.modules.user.models import User
from src.modules.user.repository import user_repository_dependency
from src.modules.user.schema import JwtPayload
from src.modules.user.schema import LoginDto
from src.modules.user.schema import SignupDto


class UserService:
    def __init__(self, user_repository: user_repository_dependency) -> None:
        self.user_repository = user_repository

    def login(self, login_dto: LoginDto):
        user = self.user_repository.get_user_by_email(login_dto.email)
        passwords_match = (
            self.verify_password(login_dto.password, user.password) if user else False
        )
        if not user or not passwords_match:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "Invalid email or password"},
            )
        jwt_token = self.generate_jwt(user)
        return jwt_token

    def signup(self, signup_dto: SignupDto):
        existing = self.user_repository.get_user_by_email(signup_dto.email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "Account already exists"},
            )
        hashed_password = self.hash_password(signup_dto.password)
        signup_dto.password = hashed_password
        user = self.user_repository.create_user(signup_dto)
        jwt_token = self.generate_jwt(user)
        return jwt_token

    def get_user(self, user_id: str):
        return self.user_repository.get_user_by_id(user_id)

    def get_users(self):
        return self.user_repository.get_users()

    def hash_password(self, password: str):
        salt = bcrypt.gensalt(10)
        return bcrypt.hashpw(bytes(password, "utf-8"), salt).decode("utf-8")

    def verify_password(self, password: str, hash_password: str):
        return bcrypt.checkpw(bytes(password, "utf-8"), bytes(hash_password, "utf-8"))

    def generate_jwt(self, user: User):
        payload = JwtPayload(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        return self.user_repository.generate_jwt(payload)


user_service_dependency = Annotated[UserService, Depends(UserService)]
