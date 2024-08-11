from app.core.genericrepository import GenericRepository, GenericSqlRepository
from app.repository.models import iotSensorData
from abc import ABC, abstractmethod
from typing import Optional
from sqlmodel import Session, select, and_


class iotSensorReposityBase(GenericRepository[iotSensorData], ABC):
    """iotSensor repository.
    """
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[iotSensorData]:
        raise NotImplementedError()



class HeroRepository(GenericSqlRepository[iotSensorData], iotSensorReposityBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, iotSensorData)

    def get_by_name(self, macid: str) -> Optional[iotSensorData]:
        stmt = select(iotSensorData).where(iotSensorData.sensor_mac_id == macid)
        return self._session.exec(stmt).first()
