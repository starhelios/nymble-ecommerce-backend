from fastapi import APIRouter

from src.middlewares.auth import auth_dependency
from src.modules.user.schema import LoginDto
from src.modules.user.schema import SignupDto
from src.modules.user.schema import UserResponse
from src.modules.user.service import user_service_dependency

users = APIRouter(prefix="/api/users", tags=["users"])


@users.post("/login")
def login(user_service: user_service_dependency, login_dto: LoginDto):
    return user_service.login(login_dto)


@users.post("/signup")
def signup(user_service: user_service_dependency, signup_dto: SignupDto):
    return user_service.signup(signup_dto)


@users.get("/", response_model=UserResponse)
def get_user(
    user_service: user_service_dependency,
    user: auth_dependency,
):
    return user_service.get_user(user.id)


@users.get("/users", response_model=list[UserResponse])
def get_users(user_service: user_service_dependency):
    return user_service.get_users()
