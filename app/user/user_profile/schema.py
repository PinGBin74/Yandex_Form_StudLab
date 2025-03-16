from typing import Optional

from pydantic import BaseModel



class CreateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
