from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, Optional, List
from app.core.genericmodel import BaseModel
from app.core.genericrepository import GenericRepository
from sqlmodel.sql.expression import SelectOfScalar
from sqlmodel import SQLModel, Session, select, and_ 

T = TypeVar("T", bound=BaseModel)


class GenericServiceBase(Generic[T], ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError()

    @abstractmethod
    def list(self, **filters) -> List[T]:
        raise NotImplementedError()

    @abstractmethod
    def add(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def update(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError()



class GenericService(GenericServiceBase[T], ABC):
    def __init__(self, repository: GenericRepository, model_cls: Type[T]) -> None:
        self._repository = repository
        self._model_cls = model_cls
 
    def get_by_id(self, id: int):  # -> Optional[T]:
        stmt = self._repository.get_by_id(id)
        return stmt

    def list(self, **filters) -> List[T]:
        stmt = self._repository.list(**filters)
        return stmt

    def add(self, record: T) -> T:
        stmt = self._repository.add(record)
        return stmt

    def update(self, record: T) -> T:
        stmt = self._repository.add(record)
        return stmt

    def delete(self, id: int) -> None:
        self._repository.delete(id)
