#from sqlalchemy.engine import base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, DateTime
from sqlalchemy.dialects.mysql import JSON
from app.core.database import Base
#from geoalchemy2 import Geometry
from sqlalchemy.sql import func


#iotSensorData
class iotSensorData(Base):
    __tablename__ = "iot_sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_mac_id = Column(String)
    # sensor_purpose = Column(String)
    # sensor_location = Column(Geometry('POINT'))
    sensor_data = Column(JSON)
    created_user = Column(String)
    created_date = Column(DateTime, default=func.current_timestamp())
    # updated_user = Column(String)
