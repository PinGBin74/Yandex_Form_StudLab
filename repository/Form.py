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
        with self.db_session() as session:
            session.add(form_model)
            session.commit()
        return form_model.id

    def delete_form(self, form_id: int, user_id: int) -> None:
        query = delete(Form).where(Form.id == form_id, Form.user_id == user_id)
        with self.db_session() as session:
            session.execute(query)
            session.commit()

    def update_form_title(self, form_id: int, title: str) -> Optional[Form]:
        query = (
            update(Form)
            .where(Form.id == form_id)
            .valeus(title=title)
            .returning(Form.id)
        )
        with self.db_session() as session:
            form_id: int = session.execute(query).scalar()
            session.commit()
            session.flush()
        return self.get_form(form_id)
