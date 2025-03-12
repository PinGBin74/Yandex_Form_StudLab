from typing import Optional

from pydantic import BaseModel


class UserLogin(BaseModel):
    user_id: int
    access_token: str


class CreateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
