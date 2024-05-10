from fastapi import APIRouter
from app.apis.iotdata import iotdata
from app.apis.jsonforms import jsonforms


api_router = APIRouter()
api_router.include_router(iotdata.iotdata_router, prefix="/iotdata")
api_router.include_router(jsonforms.jsonforms_router, prefix="/jsonforms")
