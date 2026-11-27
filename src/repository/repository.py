from abc import ABC, abstractmethod
from typing import Any


class Repository(ABC):

    @abstractmethod
    def create(self, **kwargs): pass
    @abstractmethod
    def readOne(self, column_name, column_data): pass
    @abstractmethod
    def readAll(self): pass
    @abstractmethod
    def update(self, table_id, column, new_data): pass
    @abstractmethod
    def delete(self, table_id): pass