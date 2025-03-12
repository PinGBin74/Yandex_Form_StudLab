from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from dependecy import get_auth_service
from exception import UserNotFoundException, UserNotCorrectPasswordException
from schema.user import UserLogin, CreateUser
from service.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=UserLogin)
async def login(
    body: CreateUser,
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    try:
        return auth_service.login(body.username, body.password)

    except UserNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except UserNotCorrectPasswordException as e:
        raise HTTPException(status_code=403, detail=str(e))
