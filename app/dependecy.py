from fastapi import Depends, security,Security, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db_session
from app.exception import TokenExpired, TokenNotCorrect
from app.form.repository import FormRepository
from app.user.user_profile.repository import UserRepository
from app.user.user_profile.service import UserService
from app.settings import Settings
from app.form.service import FormService
from app.user.auth.service import AuthService


async def get_form_repository(
    db_session: Session = Depends(get_db_session),
) -> FormRepository:
    return FormRepository(db_session)


async def get_form_service(
    form_repository: FormRepository = Depends(get_form_repository),
) -> FormService:
    return FormService(form_repository=form_repository)


async def get_user_repository(
    db_session: Session = Depends(get_db_session),
) -> UserRepository:
    return UserRepository(db_session=db_session)


async def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repository=user_repository, settings=Settings())


async def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
    auth_service: AuthService = Depends(get_auth_service),
) -> UserService:
    return UserService(user_repository=user_repository, auth_service=auth_service)


reusable_oauth2 = security.HTTPBearer()


async def get_request_user_id(
    auth_service: AuthService = Depends(get_auth_service),
    token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
) -> int:
    try:
        user_id = auth_service.get_user_id_from_access_token(token.credentials)

    except TokenExpired as e:
        raise HTTPException(status_code=401, detail=str(e))

    except TokenNotCorrect as e:
        raise HTTPException(status_code=401, detail=str(e))

    return user_id
