from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import Settings
import logging
from typing import Callable
from sqlmodel import create_engine, Session


setings = Settings()
logger = logging.getLogger("iotAPP") #{__name__}
logger.setLevel(logging.INFO)
# Declare base for model
Base = declarative_base()

# create database engine
# get database session

def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        logger.info(setings.DATABASE_URI)
        engine = create_engine(setings.DATABASE_URI, pool_pre_ping=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_sqlmodel_engine(settings: Settings, **kwargs):
    logger.info(settings.DATABASE_URI)
    #settings.database_connection_str
    return create_engine(settings.DATABASE_URI, **kwargs)


def sqlmodel_session_maker(engine) -> Callable[[], Session]:
    return lambda: Session(bind=engine, autocommit=False, autoflush=False)
