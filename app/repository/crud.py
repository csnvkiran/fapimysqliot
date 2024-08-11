# from typing import List
# from sqlalchemy import text
# from sqlalchemy.orm import defer, undefer, load_only
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.core.exceptions import (
    EntityInfoException,
    EntityInfoNotFoundError,
    EntityInfoInfoAlreadyExistError,
)
from app.repository.schemas import (
    PaginatedInfo,
    Interval,
)
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd 
import logging


class crud_repository:
    def __init__(self, entity):
        self.entity = entity

    # Function to get list of car info
    def get_all(self, session: Session):
         #session : Session = session
        return session.query(self.entity).all()

    def get_pagination(self, session: Session, filter:PaginatedInfo):
        # session : Session = session
        if filter.descending:
            return  session.query(self.entity).order_by(self.entity.id.desc()).limit(filter.limit).offset(filter.offset).all()    
        return  session.query(self.entity).order_by(self.entity.id.asc()).limit(filter.limit).offset(filter.offset).all()

    def get_intervals(self, session: Session, interval: Interval, limit:int=0):
        logging.debug(msg="test")
        session : Session = session
        current_datetime = datetime.now()
        current_date = date.today()
        match interval:
            case Interval.minutes:
                filter_date = current_datetime + relativedelta(minutes=-limit)
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date).all()    

            case Interval.hours:
                filter_date_max = current_datetime.replace(second=0, microsecond=0, minute=0, hour=current_datetime.hour) + relativedelta(hours=-limit)
                filter_date_min = current_datetime.replace(second=0, microsecond=0, minute=0, hour=current_datetime.hour) #+timedelta(hours=current_datetime.minute//30) #+ relativedelta(hours=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(and_(self.entity.created_date < filter_date_min, self.entity.created_date >= filter_date_max)).all()    

            case Interval.days:
                filter_date_max = current_date + relativedelta(days=-limit)
                filter_date_min = current_date # + relativedelta(days=-limit)
                #print(filter_date_max)
                #print(filter_date_min)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(and_(self.entity.created_date < filter_date_min, self.entity.created_date >= filter_date_max)).all()    
 
            case Interval.weeks:
                filter_date_min = current_date - timedelta(days=current_date.weekday())
                filter_date_max = filter_date_min + relativedelta(weeks=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_min).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(and_(self.entity.created_date < filter_date_min, self.entity.created_date >= filter_date_max)).all()    
 
            case Interval.months:
                filter_date_min = current_date - timedelta(days=current_date.day-1)
                filter_date_max = filter_date_min + relativedelta(months=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_min).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(and_(self.entity.created_date < filter_date_min, self.entity.created_date >= filter_date_max)).all()    

            case Interval.years:
                filter_date = current_date - timedelta(days=current_date.day-1)
                filter_date_min = filter_date - relativedelta(months=(filter_date.month-1))
                filter_date_max = filter_date_min + relativedelta(years=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_min).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(and_(self.entity.created_date < filter_date_min, self.entity.created_date >= filter_date_max)).all()    
            
            case _:
                filter_date = current_date + relativedelta(minutes=-5)
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date).all()    

    #Furtion to get invervals from current datetime
    def get_intervals_from_nowon(self, session: Session, interval: Interval, limit:int=0):
        # session : Session = session
        current_datetime = datetime.now()
        current_date = date.today()
        match interval:
            case Interval.minutes:
                filter_date = current_datetime + relativedelta(minutes=-limit)
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date).all()    

            case Interval.hours:
                filter_date_max = current_datetime.replace(second=0, microsecond=0, minute=0, hour=current_datetime.hour) + relativedelta(hours=-limit)
                filter_date_min = current_datetime.replace(second=0, microsecond=0, minute=0, hour=current_datetime.hour) #+ timedelta(hours=current_datetime.minute//30) #+ relativedelta(hours=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_min).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    

            case Interval.days:
                filter_date_max = current_date + relativedelta(days=-limit)
                filter_date_min = current_date # + relativedelta(days=-limit)
                #print(filter_date_max)
                #print(filter_date_min)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    
 
            case Interval.weeks:
                filter_date_min = current_date - timedelta(days=current_date.weekday())
                filter_date_max = filter_date_min + relativedelta(weeks=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_min).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    
 
            case Interval.months:
                filter_date_min = current_date - timedelta(days=current_date.day-1)
                filter_date_max = filter_date_min + relativedelta(months=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_min).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    

            case Interval.years:
                filter_date = current_date - timedelta(days=current_date.day-1)
                filter_date_min = filter_date - relativedelta(months=(filter_date.month-1))
                filter_date_max = filter_date_min + relativedelta(years=-limit)
                if limit==0:
                    return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_min).all()    
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date_max).all()    
            
            case _:
                filter_date = current_date + relativedelta(minutes=-5)
                return  session.query(self.entity).order_by(self.entity.id.desc()).filter(self.entity.created_date >= filter_date).all()    


    def get_usr_intervals(self, session: Session, startdate: datetime = datetime.now(), enddate: datetime = datetime.now()-relativedelta(minutes=5) ):
        # session : Session = session
        return session.query(self.entity).order_by(self.entity.id.desc()).filter(and_(self.entity.created_date <= enddate, self.entity.created_date >= startdate)).all()    



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
