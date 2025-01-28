#from sqlalchemy.engine import base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, DateTime
from sqlalchemy.dialects.mysql import JSON
from app.core.database import Base
#from geoalchemy2 import Geometry
from sqlalchemy.sql import func


#jsonSchemaFormType
class jsonSchemaFormType(Base):
    __tablename__ = "lkup_jsonSchemaFormType"

    id = Column(Integer, primary_key=True, index=True)
    lkup_code = Column(String)
    lkup_lang = Column(String)
    lkup_description = Column(String)
    activStatus = Column(String)
    created_user = Column(String)
    created_date = Column(DateTime, default=func.current_timestamp())
    updated_user = Column(String)
    updated_date = Column(DateTime, default=func.current_timestamp())


#jsonSchemaForms
class jsonSchemaForms(Base):
    __tablename__ = "jsonSchemaForms"

    id = Column(Integer, primary_key=True, index=True)
    jsonSchemaFormCode = Column(String)
    jsonSchemaFormName = Column(String)
    jsonSchemaFormType = Column(String)
    jsonSchemaFormVersion = Column(String)
    jsonSchema = Column(JSON)
    jsonSchemaUI = Column(JSON)
    jsonSchemaFormData = Column(JSON)
    activStatus = Column(String)
    created_user = Column(String)
    created_date = Column(DateTime, default=func.current_timestamp())
    updated_user = Column(String)
    updated_date = Column(DateTime, default=func.current_timestamp())


class jsonSchemaFormDataSubmit(Base):
    __tablename__ = "jsonSchemaFormDataSubmit"

    id = Column(Integer, primary_key=True, index=True)
    jsonSchemaFormCode = Column(String)
    jsonSchemaFormData = Column(JSON)
    activStatus = Column(String)
    created_user = Column(String)
    created_date = Column(DateTime, default=func.current_timestamp())
    updated_user = Column(String)
    updated_date = Column(DateTime, default=func.current_timestamp())

