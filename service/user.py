import string
from dataclasses import dataclass
from http.client import HTTPException

from repository.user import UserRepository
from schema import UserLogin, CreateUser
from service.auth import AuthService


@dataclass
class UserService:
    user_repository: UserRepository
    auth_service: AuthService

    def create_user(self, username: str, password: str) -> UserLogin:
        create_user_obj = CreateUser(username=username, password=password)
        user = self.user_repository.create_user(create_user_obj)
        access_token = self.auth_service.generate_access_token(user_id=user.id)
        return UserLogin(user_id=user.id, access_token=access_token)
