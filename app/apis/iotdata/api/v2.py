from fastapi import APIRouter, Depends, Query
import logging
from app.core.config import Settings
from app.repository.models import iotSensorData
from app.core.database import create_sqlmodel_engine, sqlmodel_session_maker
from app.core.database import get_db
from sqlmodel import SQLModel
from sqlmodel.pool import StaticPool

from typing import Callable
from sqlmodel import Session

from app.repository.iotservice import iotSensorService



router = APIRouter()

settings = Settings()
engine = create_sqlmodel_engine(settings=settings, poolclass=StaticPool)
SQLModel.metadata.create_all(engine)
session_maker = sqlmodel_session_maker(engine)
#session = session_maker()
logger = logging.getLogger("iotAPP") #{__name__}
logger.setLevel(logging.INFO)



@router.get("/{id}")
async def getlookup(id:int = 1):
    return id


@router.get("/DataById/{id}")
async def getlookup(id:int):
    _session = session_maker()
    service =  iotSensorService(_session)
    iotdata: iotSensorData = service.get_by_id(id)
    _session.close()
    return iotdata



@router.get("/DataByMacId/{name}")
async def getlookup(name:str):
    _session = session_maker()
    service =  iotSensorService(_session)
    iotdata: iotSensorData = service.get_by_name(name)
    _session.close()
    return iotdata



@router.get("/DatabelowID/{id}")
async def getlookup(id:int):
    _session = session_maker()
    service =  iotSensorService(_session)
    iotdata: iotSensorData = service.list(id <= 15)
    _session.close()
    return iotdata