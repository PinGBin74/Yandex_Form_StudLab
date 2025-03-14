from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update
from models import Form
from schema.form import FormCreateSchema
from typing import Optional, List


class FormRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_forms(self) -> List[Form]:
        async with self.db_session.begin():
            result = await self.db_session.execute(select(Form))
            return result.scalars().all()

    async def get_form(self, form_id: int) -> Optional[Form]:
        async with self.db_session.begin():
            result = await self.db_session.execute(
                select(Form).where(Form.id == form_id)
            )
            return result.scalars().first()

    async def create_form(self, form: FormCreateSchema, user_id: int) -> int:
        fields_as_dicts = [field.model_dump() for field in form.fields]
        form_model = Form(
            title=form.title,
            fields=fields_as_dicts,
            user_id=user_id,
        )
        async with self.db_session as session:  # создаём новую сессию
            async with session.begin():
                session.add(form_model)
                await session.flush()  # гарантируем, что id сгенерирован
                await session.refresh(form_model)  # обновляем объект внутри транзакции
        return form_model.id
    async def delete_form(self, form_id: int, user_id: int) -> None:
        async with self.db_session.begin():
            await self.db_session.execute(
                delete(Form).where(Form.id == form_id, Form.user_id == user_id)
            )
            await self.db_session.commit()

    async def update_form_title(self, form_id: int, title: str) -> Optional[Form]:
        async with self.db_session.begin():
            result = await self.db_session.execute(
                update(Form)
                .where(Form.id == form_id)
                .values(title=title)
                .returning(Form.id)
            )
            updated_form_id = result.scalar()
            await self.db_session.commit()

        return await self.get_form(updated_form_id) if updated_form_id else None

    async def get_user_form(self, form_id: int, user_id: int) -> Optional[Form]:
        async with self.db_session.begin():
            result = await self.db_session.execute(
                select(Form).where(Form.id == form_id, Form.user_id == user_id)
            )
            return result.scalars().first()

    async def get_form_by_id(self, form_id: int) -> Optional[Form]:
        async with self.db_session.begin():
            result = await self.db_session.execute(
                select(Form).where(Form.id == form_id)
            )
            return result.scalars().first()
