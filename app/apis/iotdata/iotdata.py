from fastapi import APIRouter
from app.apis.iotdata.api import v1


iotdata_router = APIRouter()
iotdata_router.include_router(v1.router, prefix="/v1", tags=["iotdata_v1"])
