from fastapi import FastAPI, Request, Response, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.config import settings
from app.apis import apis
import logging


app = FastAPI(
    title=settings.PROJECT_NAME,
    # root_path="/proxy/8000",
    openapi_url=f"{settings.API_STR}/openapi.json"
    # removed /vscode
)


logging.info("starting service")

app.include_router(apis.api_router, prefix=settings.API_STR)
