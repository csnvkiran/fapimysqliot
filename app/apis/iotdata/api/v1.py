from sqlalchemy.orm import Session
from app.core.database import get_db
from fastapi import APIRouter, Depends, Query
from app.repository.schemas import (
    IOTData,
    createIOTData,
    PaginatedInfo,
    IOTDataPaginatedInfo,
    Interval,
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
    # for i in retvalue:
    #     logger.info(i.sensor_data)
    #     logger.info(type(i.sensor_data))
    return retvalue



@router.get("/iotdatapaging/", response_model=IOTDataPaginatedInfo)
async def getiotdatafilter(
        offset: int = 0,
        limit: int = 10,
        descending: bool = True,
        session: Session = Depends(get_db)
    ):
    entitycrud = crud_repository(iotSensorData)
    filter = PaginatedInfo(limit=limit, offset=offset, descending=descending)
    retdata = entitycrud.get_pagination(session, filter)
    # for i in retvalue:
    #     logger.info(i.sensor_data)
    #     logger.info(type(i.sensor_data))
    retvalue = IOTDataPaginatedInfo(limit=limit, offset=offset, data=retdata)
    return retvalue



@router.get("/iotdataintervals/", response_model=List[IOTData])
async def getiotdatainter(
        interval: Interval = Interval.minutes,
        limit:int = 5,
        fromnowon: bool = False, 
        session: Session = Depends(get_db)
    ):
    entitycrud = crud_repository(iotSensorData)
    if fromnowon:
        retdata = entitycrud.get_intervals_from_nowon(session, interval, limit)    
    else:   
        retdata = entitycrud.get_intervals(session, interval, limit)
    # for i in retvalue:
    #     logger.info(i.sensor_data)
    #     logger.info(type(i.sensor_data))
    
    retvalue = retdata
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
