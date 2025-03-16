from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException

from app.exception import FormNotFound
from app.form.schema import FormCreateSchema, JSON, FormSchema

from app.form.service import FormService
from app.dependecy import get_form_service, get_request_user_id

router = APIRouter(prefix="/form", tags=["form"])


@router.get("/all", response_model=list[FormSchema])
async def get_forms(form_service: Annotated[FormService, Depends(get_form_service)]):
    form = await form_service.get_forms()
    return form


@router.get("/{form_id}", response_model=FormSchema)
async def search_form(
    form_id: int,
    form_service: FormService = Depends(get_form_service),
):
    try:
        return await form_service.get_form_by_id(form_id=form_id)
    except FormNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/create", response_model=FormSchema)
async def create_form(
    body: FormCreateSchema,
    form_service: Annotated[FormService, Depends(get_form_service)],
    user_id: int = Depends(get_request_user_id),
):
    form = await form_service.create_form(body, user_id)
    return form


@router.patch("/{form_id}", response_model=FormSchema)
async def patch_form(
    form_id: int,
    title: str,
    form_service: Annotated[FormService, Depends(get_form_service)],
    user_id: int = Depends(get_request_user_id),
):
    try:
        return await form_service.update_form_title(
            form_id=form_id, title=title, user_id=user_id
        )

    except FormNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)


@router.delete("/{form_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_form(
    form_id: int,
    form_service: Annotated[FormService, Depends(get_form_service)],
    user_id: int = Depends(get_request_user_id),
):
    try:
        await form_service.delete_form(form_id=form_id, user_id=user_id)

    except FormNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
