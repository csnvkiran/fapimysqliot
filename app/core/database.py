# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import logging
from typing import Callable
from sqlmodel import create_engine, Session


logging.info(settings.DATABASE_URI)

# Declare base for model
# Base = declarative_base()

# create database engine
# engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# get database session
# def get_db():
#     """
#     Function to generate db session
#     :return: Session
#     """
#     db = None
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()


def create_sqlmodel_engine(settings: Settings, **kwargs):
    return create_engine(settings.database_connection_str, **kwargs)


def sqlmodel_session_maker(engine) -> Callable[[], Session]:
    return lambda: Session(bind=engine, autocommit=False, autoflush=False)
