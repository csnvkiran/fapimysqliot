from fastapi import APIRouter
from app.apis.iotdata import iotdata



api_router = APIRouter()
api_router.include_router(iotdata.iotdata_router,
                          prefix="/iotdata", tags=["lookup"])
