from fastapi import APIRouter
from app.apis.jsonforms.api import v1


jsonforms_router = APIRouter()
jsonforms_router.include_router(v1.router, prefix="/v1", tags=["jsonforms_v1"])
