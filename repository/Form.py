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
            form: Form = (
                session.execute(select(Form).where(Form.id == form_id))
                .scalars()
                .first()
            )
        return form

    def create_form(self, form: FormCreateSchema, user_id: int) -> int:
        fields_as_dicts = [field.model_dump() for field in form.fields]
        form_model = Form(
            title=form.title,
            fields=fields_as_dicts,
            user_id=user_id,
        )
        with self.db_session() as session:
            session.add(form_model)
            session.commit()
            session.refresh(form_model)
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
            .values(title=title)
            .returning(Form.id)
        )
        with self.db_session() as session:
            form_id: int = session.execute(query).scalar()
            session.commit()
            session.flush()
        return self.get_form(form_id)

    def get_user_form(self, form_id: int, user_id: int) -> Optional[Form]:
        query = select(Form).where(Form.id == form_id, Form.user_id == user_id)
        with self.db_session() as session:
            form: Form = session.execute(query).scalar_one_or_none()
        return form

    def get_form_by_id(self, form_id: int) -> Optional[Form]:
        query = select(Form).where(Form.id == form_id)
        with self.db_session() as session:
            form: Form = session.execute(query).scalar()
        return form
