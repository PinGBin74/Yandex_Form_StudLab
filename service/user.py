from dataclasses import dataclass
from schema import UserLogin, CreateUser
from repository.user import UserRepository
from service.auth import AuthService
from fastapi import HTTPException, status
from exception import UserAlreadyExists


@dataclass
class UserService:
    user_repository: UserRepository
    auth_service: AuthService

    async def create_user(self, username: str, password: str) -> UserLogin:
        create_user_obj = CreateUser(username=username, password=password)
        try:
            user = await self.user_repository.create_user(create_user_obj)
        except UserAlreadyExists as e:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
        access_token = self.auth_service.generate_access_token(user_id=user.id)
        return UserLogin(user_id=user.id, access_token=access_token)
