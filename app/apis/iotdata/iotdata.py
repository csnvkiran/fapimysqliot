from fastapi import APIRouter
from app.apis.iotdata.api import v1
from app.apis.iotdata.api import v2


iotdata_router = APIRouter()
iotdata_router.include_router(v1.router, prefix="/v1", tags=["iotdata_v1"])
iotdata_router.include_router(v2.router, prefix="/v2", tags=["iotdata_v2"])
