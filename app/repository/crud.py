# from typing import List
# from sqlalchemy import text
# from sqlalchemy.orm import defer, undefer, load_only
from sqlalchemy.orm import Session
from app.core.exceptions import (
    EntityInfoException,
    EntityInfoNotFoundError,
    EntityInfoInfoAlreadyExistError,
)


class crud_repository:
    def __init__(self, entity):
        self.entity = entity

    # Function to get list of car info
    def get_all(self, session: Session):
        # session : Session = session
        return session.query(self.entity).all()

    # Function to add a new car info to the database
    def create_entity(self, session: Session, newmodel):
        # gender_details = session.query(entity).filter(lamdba x: xfilter).first()
        # if gender_details is not None:
        #     raise EntityInfoInfoAlreadyExistError

        new_entity = self.entity(**newmodel.dict())
        new_entity.created_user = "API"
        session.add(new_entity)
        session.commit()
        session.refresh(new_entity)
        return new_entity

    # Function to update details of the car
    # def update_entity(self, session: Session, _code: str, info_update):
    #     curentity = self.get_entity_by_code(session, _code)

    #     if curentity is None:
    #         raise GenderInfoNotFoundError

    #     curentity.dto2entity(info_update)

    #     session.commit()
    #     session.refresh(curentity)

    #     return curentity
