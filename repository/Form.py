from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from models import Form
from schema.form import FormCreateSchema
from typing import Optional, List


class FormRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_forms(self) -> List[Form]:
        with self.db_session() as session:
            form: list[Form] = session.execute(select(Form)).scalars().all()
        return form

    def get_form(self, form_id: int) -> Optional[Form]:
        with self.db_session() as session:
            form: Form = session.execute(select(Form)).scalars().first()
        return form

    def create_form(self, form: FormCreateSchema, user_id: int) -> int:
        form_model = Form(
            title=form.title,
            fields=form.fields,
            user_id=user_id,
        )
        self.db_session.add(form_model)
        self.db_session.commit()
        self.db_session.refresh(form_model)
        return form_model.id

    def delete_form(self, form_id: int) -> None:
        self.db_session.execute(delete(Form).where(Form.id == form_id))
        self.db_session.commit()

    def update_form_title(self, form_id: int, title: str) -> Optional[Form]:
        self.db_session.execute(
            update(Form).where(Form.id == form_id).values(title=title)
        )
        self.db_session.commit()
        return self.get_form(form_id)
