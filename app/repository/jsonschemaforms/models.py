from sqlalchemy.engine import base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, DateTime
from sqlalchemy.dialects.mysql import JSON
from app.core.database import Base
from geoalchemy2 import Geometry
from sqlalchemy.sql import func


class jsonSechema(Base):
    __tablename__ = "mdgn_jsonforms"

    id = Column(Integer, primary_key=True, index=True)
    projectCode = Column(String)
    moduleCode = Column(String)

    formCode = Column(String)
    formVersion = Column(String)
    CodformName = Column(String)

    jsonSchema = Column(JSON)
    jsonSchemaUIEdit = Column(JSON)
    jsonSchemaUIView = Column(JSON)
    jsonSchemaDefaultData = Column(JSON)
    jsonSchemaValidation = Column(JSON)

    activeStatus = Column(String)

    createdUser = Column(String)
    createdOn = Column(DateTime, default=func.current_timestamp())
    updatedUser = Column(String)
    updatedOn = Column(DateTime, default=func.current_timestamp())
