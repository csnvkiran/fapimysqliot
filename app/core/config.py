from pathlib import Path
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv
from typing import Any, Dict, Optional
from pydantic import BaseModel, ValidationError, ValidationInfo, field_validator


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

    @field_validator("DATABASE_URI") #, mode="before"
    def passwords_match(cls, v: str, info: ValidationInfo) -> str:
        # if "password1" in info.data and v != info.data["password1"]:
        #     raise ValueError("passwords do not match")
        # return v
    
        if isinstance(v, str):
            return v
           
        return (
            f"mysql+pymysql://{info.data['mysql_user']}:{info.data['mysql_password']}@{info.data['mysql_host']}:"
            f"{info.data['mysql_port']}/{info.data['mysql_database']}"
        )

    # @field_validator("DATABASE_URI", mode="before") #
    # def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo, values: Dict[str, Any]) -> Any:
    #     if isinstance(v, str):
    #         return v
           
    #     return (
    #         f"mysql+pymysql://{values['mysql_user']}:{values['mysql_password']}@{values['mysql_host']}:"
    #         f"{values['mysql_port']}/{values['mysql_database']}"
    #     )


settings = Settings()
