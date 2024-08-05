from pathlib import Path
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv
from typing import Any, Dict, Optional
from pydantic import validator


load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )
    mysql_user: str
    mysql_password: str
    mysql_host: str
    mysql_port: str
    mysql_database: str
    PROJECT_NAME: Optional[str] = "Klea iot APIs"
    API_STR: Optional[str] = "/api"
    DATABASE_URI: Optional[str] = None
    cors_urls: Optional[list] = ["https://*.klea.in"]

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
           
        return (
            f"mysql+pymysql://{values.get('mysql_user')}:{values.get('mysql_password')}@{values.get('mysql_host')}:"
            f"{values.get('mysql_port')}/{values.get('mysql_database')}"
        )


settings = Settings()
