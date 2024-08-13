from app.core.genericservice import  GenericServiceBase, GenericService
from app.repository.models import iotSensorData
from app.repository.iotrepository import iotSensorRepositoryBase, iotSensorRepository
from abc import ABC, abstractmethod
from typing import Optional
from sqlmodel import Session, select, and_


class iotSensorServiceBase(GenericServiceBase[iotSensorData], ABC):
    """iotSensor repository.
    """
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[iotSensorData]:
        raise NotImplementedError()



class iotSensorService(GenericService[iotSensorData], iotSensorServiceBase):
    def __init__(self, session: Session) -> None:
        _repository = iotSensorRepository(session)
        _session = session
        super().__init__(_repository, iotSensorData)
        

    def get_by_name(self, macid: str) -> Optional[iotSensorData]:
        stmt =  self._repository.get_by_name(macid)
        return stmt
