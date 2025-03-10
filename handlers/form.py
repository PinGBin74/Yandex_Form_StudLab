from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException


from schema import FormSchema, FormCreateSchema

from service import FormService
from dependecy import get_form_service

router = APIRouter(prefix="/form", tags=["form"])


@router.get("/all", response_model=list[FormSchema])
async def get_forms(form_service: Annotated[FormService, Depends(get_form_service)]):
    return form_service.get_tasks()


# @router.post("/create", response_model=FormSchema)
# async def create_form(body: FormCreateSchema, form_service:Annotated[FormService, Depends(get_form_service)],
#                       user_id:int=Depends(get_request_user_id)):
#     form=form_service.create_form(body, user_id)
#     return form
