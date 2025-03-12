from exception import FormNotFound
from repository import FormRepository
from schema import FormSchema, FormCreateSchema
from dataclasses import dataclass


@dataclass
class FormService:
    form_repository: FormRepository

    def get_forms(self) -> list[FormSchema]:
        forms = self.form_repository.get_forms()
        return [FormSchema.model_validate(form) for form in forms]

    def create_form(self, body: FormCreateSchema, user_id: int) -> FormSchema:
        form_id = self.form_repository.create_form(body, user_id)
        form = self.form_repository.get_form(form_id)
        return FormSchema.model_validate(form)

    def update_form_title(self, form_id: int, title: str, user_id: int) -> FormSchema:
        form = self.form_repository.get_form(form_id)
        if not form or form.user_id != user_id:
            raise FormNotFound
        form = self.form_repository.update_form_title(form_id=form_id, title=title)
        return FormSchema.model_validate(form)

    def delete_form(self, form_id: int, user_id: int) -> None:
        form = self.form_repository.get_form(form_id)
        if not form or form.user_id != user_id:
            raise FormNotFound
        self.form_repository.delete_form(form_id=form_id, user_id=user_id)
