from pydantic.types import BaseModel, Json, validator
from typing import Optional, List
from typing import Dict, Any
from fastapi import Query
from shapely import Point
from datetime import date, datetime
import json
import logging
from enum import Enum


logger = logging.getLogger(__name__)


# create jsonstring
def create_jsonstr(v, values):
    if v is not None:
        try:
            return json.dumps(v)
        except Exception as e:
            logging.Logger.debug("Failed creating json:  %v -- %d", v, e)
    else:
        pass

    return None


# TO support creation and update APIs
class CreateAndUpdateJsonForm(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    sensor_mac_id: Optional[str]
    # sensor_purpose: Optional[str]
    # sensor_location: Optional[Point]
    sensor_data: Optional[Json]
    created_user: Optional[str]
    # updated_user: Optional[str]

    _validate_json = validator("sensor_data", pre=True, always=True, allow_reuse=True)(
        create_jsonstr
    )


# Crud
class createIOTData(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    sensor_mac_id: Optional[str]
    sensor_data: Optional[Dict[str, Any]]


# cRud
class ReadIOTData(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    sensor_mac_id: Optional[str]
    sensor_data: Optional[Json]
    created_date: Optional[datetime]

    _validate_json = validator("sensor_data", pre=True, always=True, allow_reuse=True)(
        create_jsonstr
    )


# TO support list and get APIs
class IOTData(ReadIOTData):
    id: Optional[int]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class PaginatedInfo(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    limit: Optional[int]
    offset: Optional[int]
    descending: bool = False
