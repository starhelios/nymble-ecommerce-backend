import re

from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr
from pydantic import ValidationError
from pydantic import validator


class LoginDto(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=50)

    @validator("password")
    def validate_password(cls, value):
        if not re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]", value
        ):
            raise ValidationError(
                "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"
            )
        return value


class SignupDto(BaseModel):
    first_name: constr(min_length=5, max_length=255)
    last_name: constr(min_length=5, max_length=255)
    email: EmailStr
    password: constr(min_length=8, max_length=50)

    @validator("password")
    def validate_password(cls, value):
        if not re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]", value
        ):
            raise ValidationError(
                "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"
            )
        return value


class JwtPayload(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str


class UserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
