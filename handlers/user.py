from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from dependecy import get_user_service
from schema import CreateUser, UserLogin
from service.user import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserLogin)
async def create_user(
    body: CreateUser,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.create_user(body.username, body.password)
