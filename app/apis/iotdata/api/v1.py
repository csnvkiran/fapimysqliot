from sqlalchemy.orm import Session
from app.core.database import get_db
from fastapi import APIRouter, Depends
from app.repository.schemas import (
    IOTData,
    createIOTData,
    CreateAndUpdateIOTData,
    IOTDataPaginatedInfo,
)
from app.repository.models import iotSensorData
from typing import List
from app.repository.crud import crud_repository
import sys
import logging


router = APIRouter()

logger = logging.getLogger("{__name__}")
logger.setLevel(logging.DEBUG)
# session: Session = Depends(get_db)
stdoutHandler = logging.StreamHandler(stream=sys.stdout)
# Set the log levels on the handlers
stdoutHandler.setLevel(logging.DEBUG)
logger.addHandler(stdoutHandler)


@router.get("/")
async def getlookup():
    return "service from iot api"


@router.get("/iotdata", response_model=List[IOTData])
async def getlookup(session: Session = Depends(get_db)):
    entitycrud = crud_repository(iotSensorData)
    retvalue = entitycrud.get_all(session)
    for i in retvalue:
        logger.info(i.sensor_data)
        logger.info(type(i.sensor_data))
    return retvalue


@router.post("/submitiotdata")
async def postservice(fuser: createIOTData, session: Session = Depends(get_db)):
    entitycrud = crud_repository(iotSensorData)
    # fuser.created_user = "API"
    # logger.info(fuser.sensor_data)
    # logger.info(type(fuser.sensor_data))
    return entitycrud.create_entity(session, fuser)


# @router.put("/updateiotdata")
# async def putservice(fuser: CreateAndUpdateIOTData, session: Session = Depends(get_db)):
#      entitycrud = crud_repository(iotSensorData)
#     return entitycrud.update_entity(session, f"user_name = '{fuser.user_name}'", fuser)
