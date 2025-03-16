from typing import Annotated
from fastapi import APIRouter, Depends
from app.dependecy import get_user_service
from app.user.auth.schema import UserLogin
from app.user.user_profile.schema import CreateUser
from app.user.user_profile.service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserLogin)
async def create_user(
    body: CreateUser,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    return await user_service.create_user(body.username, body.password)
