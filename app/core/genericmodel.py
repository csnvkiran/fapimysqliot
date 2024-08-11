from typing import Optional, List

from sqlmodel import SQLModel, Field, Column, Integer, String, ForeignKey, Relationship

from app.core.utilities import to_camel


class BaseModel(SQLModel):
    """_summary_

    Args:
        SQLModel (_type_): _description_

    Base SQL model class.
    """

    id: Optional[int] = Field(sa_column=Column("Id", Integer, primary_key=True, autoincrement=True))

    class Config:
        alias_generator = to_camel
        populate_by_name = True
        arbitrary_types_allowed = True