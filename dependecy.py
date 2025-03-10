from fastapi import Depends, Request, security, Security, HTTPException
from sqlalchemy.orm import Session

from database import get_db_session
from repository import FormRepository

from service import FormService


def get_form_repository(
    db_session: Session = Depends(get_db_session),
) -> FormRepository:
    return FormRepository(db_session)


def get_form_service(
    form_repository: FormRepository = Depends(get_form_repository),
) -> FormService:
    return FormService(form_repository=form_repository)
