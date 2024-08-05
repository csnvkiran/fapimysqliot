from sqlalchemy.engine import base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, DateTime
from sqlalchemy.dialects.mysql import JSON
from app.core.genericmodel import BaseModel
from geoalchemy2 import Geometry
from sqlalchemy.sql import func


class iotSensorData(Base):
    __tablename__ = "iot_sensor_data"

    # id = Column(Integer, primary_key=True, index=True)
    # sensor_mac_id = Column(String)
    # # sensor_purpose = Column(String)
    # # sensor_location = Column(Geometry('POINT'))
    # sensor_data = Column(JSON)
    # created_user = Column(String)
    # created_date = Column(DateTime, default=func.current_timestamp())
    # # updated_user = Column(String)

    sensor_mac_id: str = Field(sa_column=Column("sensor_mac_id", String(30), nullable=False))
    sensor_data: str = Field(sa_column=Column("sensor_data", JSON, nullable=False))
    created_user: str = Field(sa_column=Column("created_user", String(30), nullable=False))
    created_date: DateTime= Field(sa_column=Column("created_date", DateTime, nullable=False,default=func.current_timestamp()))
    

