from typing import Annotated

from fastapi import Depends
from fastapi import Header
from fastapi import HTTPException
from fastapi import status
from jose import jwt
from jose import JWTError

from src.modules.user.schema import JwtPayload
from src.start.config import settings


def auth(token: str = Header(...)) -> JwtPayload:
    try:
        payload = jwt.decode(
            token=token,
            key=settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        return JwtPayload(**payload)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"message": "un-authorized"},
        )


auth_dependency = Annotated[JwtPayload, Depends(auth)]
