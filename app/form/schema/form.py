from typing import Optional, List
from pydantic import BaseModel, model_validator, ConfigDict
from sqlalchemy.orm import Mapped


class FieldSchema(BaseModel):
    type: str
    label: str
    options: Optional[List[str]] = None


class FormSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    fields: List[FieldSchema]
    user_id: int

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="after")
    def check_id_or_fields_is_not_none(self) -> "FormSchema":
        if self.title is None and self.fields is None:
            raise ValueError("title and fields cannot be None")
        return self


class FormCreateSchema(BaseModel):
    title: str
    fields: List[FieldSchema]
