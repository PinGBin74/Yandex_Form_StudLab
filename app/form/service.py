from app.exception import FormNotFound
from app.form.repository import FormRepository
from app.form.schema import FormSchema, FormCreateSchema
from dataclasses import dataclass


@dataclass
class FormService:
    form_repository: FormRepository

    async def get_forms(self) -> list[FormSchema]:
        forms = await self.form_repository.get_forms()
        return [FormSchema.model_validate(form) for form in forms]

    async def create_form(self, body: FormCreateSchema, user_id: int) -> FormSchema:
        form_id = await self.form_repository.create_form(body, user_id)
        form = await self.form_repository.get_form(form_id)
        return FormSchema.model_validate(form)

    async def update_form_title(
        self, form_id: int, title: str, user_id: int
    ) -> FormSchema:
        form = await self.form_repository.get_user_form(
            form_id=form_id, user_id=user_id
        )
        if not form or form.user_id != user_id:
            raise FormNotFound
        form = await self.form_repository.update_form_title(
            form_id=form_id, title=title
        )
        return FormSchema.model_validate(form)

    async def delete_form(self, form_id: int, user_id: int) -> None:
        form = await self.form_repository.get_user_form(
            form_id=form_id, user_id=user_id
        )
        if not form:
            raise FormNotFound
        await self.form_repository.delete_form(form_id=form_id, user_id=user_id)

    async def get_form_by_id(self, form_id: int) -> FormSchema:
        form = await self.form_repository.get_form_by_id(form_id=form_id)
        if not form:
            raise FormNotFound
        return FormSchema.model_validate(form)
