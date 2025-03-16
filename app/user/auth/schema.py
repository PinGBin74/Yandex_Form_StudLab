from pydantic import BaseModel


class UserLogin(BaseModel):
    user_id: int
    access_token: str
