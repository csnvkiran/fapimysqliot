from pydantic import BaseModel, Json, field_validator
from typing import Optional, List
from typing import Dict, Any
from fastapi import Query
from shapely import Point
from datetime import date, datetime
import json
import logging
from enum import Enum



logger = logging.getLogger(__name__)


def create_jsonstr(v, values) -> Json:
    if v is not None:
        try:
            return json.dumps(v)
        except Exception as e:
            logger.debug(f"Failed creating json: v={v} -- {e}")
    else:
        return None


def create_point(v, values) -> Point:
    if v is not None:
        try:
            return Point(v)
        except Exception as e:
            logger.debug(f"Failed creating point: v={v} -- {e}")
    else:
        return None


# TO support creation and update APIs
class CreateAndUpdateIOTData(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    sensor_mac_id: Optional[str]
    # sensor_purpose: Optional[str]
    # sensor_location: Optional[Point]
    sensor_data: Optional[Json]
    created_user: Optional[str]
    # updated_user: Optional[str]

    _validate_json = field_validator("sensor_data", pre=True, always=True, allow_reuse=True)(
        create_jsonstr
    )
    # _validate_json = validator("sensor_location", pre=True, always=True, allow_reuse=True)(
    #     create_point
    # )


# Crud
class createIOTData(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    sensor_mac_id: Optional[str]
    sensor_data: Optional[Dict[str, Any]]

    # created_user: Optional[str]
    # sensor_purpose: Optional[str]
    # sensor_location: Optional[Point]

    # updated_user: Optional[str]

    # _validate_json = validator("sensor_data", pre=True, always=True, allow_reuse=True)(
    #     create_jsonstr
    # )
    # _validate_json = validator("sensor_location", pre=True, always=True, allow_reuse=True)(
    #     create_point
    # )


# cRud
class ReadIOTData(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    sensor_mac_id: Optional[str]
    sensor_data: Optional[Json]
    created_date: Optional[datetime]

    _validate_json = field_validator("sensor_data", pre=True, always=True, allow_reuse=True)(
        create_jsonstr
    )


# TO support list and get APIs
class IOTData(ReadIOTData):
    id: Optional[int]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


# To support list cars API
class IOTDataPaginatedInfo(BaseModel):
    limit: int
    offset: int
    data: List[IOTData]

class PaginatedInfo(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    limit: Optional[int]
    offset: Optional[int]
    descending: bool = False

class Interval(str, Enum):
    minutes = "minutes"
    hours = "hours"
    weeks = "weeks"
    days = "days"
    months = "months"
    years = "years"

