from pydantic import BaseModel


class CreateUser(BaseModel):
    id: int
    username: str
    password: str
