import abc
from sqlalchemy.orm import DeclarativeBase, Session
from typing import Type, List, Dict, Optional


class BaseRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, entity: DeclarativeBase) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def remove(self, entity: DeclarativeBase) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def update(self, entity: DeclarativeBase, values: Dict) -> None:
        raise NotImplemented

    @abc.abstractmethod
    def get_by_id(self, table: Type, id_: int) -> Optional[DeclarativeBase]:
        raise NotImplemented

    @abc.abstractmethod
    def list(self, table: Type) -> List[Type]:
        raise NotImplemented


class SQLAlchemyRepository(BaseRepository):
    def __init__(self, session: Session):
        self.__session = session

    def list(self, table: Type) -> Optional[List[Type]]:
        return self.__session.get(table, range(1000))

    def get_by_id(self, table: Type, id_: int) -> Optional[DeclarativeBase]:
        return self.__session.get(table, id_)

    def update(self, entity: DeclarativeBase, values: Dict) -> None:
        self.__session.query(entity).update(values)
        self.__session.commit()

    def add(self, entity: DeclarativeBase) -> None:
        self.__session.add(entity)
        self.__session.commit()

    def remove(self, entity: DeclarativeBase) -> None:
        self.__session.query(entity).delete()
        self.__session.commit()


class TestRepository(BaseRepository):

    def __init__(self):
        self.__data = {}
        self.ids = {}

    def list(self, table: Type) -> Optional[List[Type]]:
        return self.__data.values()

    def get_by_id(self, table: Type, id_: int) -> Optional[DeclarativeBase]:
        return self.__data[self.ids[id_]]

    def update(self, entity: DeclarativeBase, values: Dict) -> None:
        self.__data[entity.__name__] = entity

    def add(self, entity: DeclarativeBase) -> None:
        self.__data[entity.__name__] = entity
        self.ids[len(self.__data)] = entity.__name__

    def remove(self, entity: DeclarativeBase) -> None:
        self.__data.pop(entity.__name__)
