from abc import ABC, abstractmethod
from typing import Any


class Repository(ABC):

    @abstractmethod
    def create(self, **kwargs): pass
    @abstractmethod
    def readOne(self, data: Any): pass
    @abstractmethod
    def readAll(self): pass
    @abstractmethod
    def update(self, table_id, new_data): pass
    @abstractmethod
    def delete(self, table_id): pass