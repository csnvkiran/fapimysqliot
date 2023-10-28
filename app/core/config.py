from typing import Any, Dict, Optional
from pydantic import validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    PROJECT_NAME: Optional[str] = "Klea iot APIs"
    API_STR: Optional[str] = "/api"
    mysql_user: str
    mysql_password: 
    mysql_host: str = "192.168.68.111"
    mysql_port: str = "4406"
    mysql_database: str = "dbkleaiot"
    DATABASE_URI: Optional[str] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return (
            f"mysql+pymysql://{values.get('mysql_user')}:{values.get('mysql_password')}@{values.get('mysql_host')}:"
            f"{values.get('mysql_port')}/{values.get('mysql_database')}"
        )


settings = Settings()
