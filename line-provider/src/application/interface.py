from typing import List, Optional, TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar("T")


class IRepository(ABC, Generic[T]):
    @abstractmethod
    async def add(self, **kwargs) -> T:
        """Создает новый объект и сохраняет его в базе данных."""
        ...

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[T]:
        """Возвращает объект по его идентификатору."""
        ...

    @abstractmethod
    async def filter_by(self, **kwargs) -> List[T]:
        """Возвращает список объектов, удовлетворяющих переданным критериям."""
        ...

    @abstractmethod
    async def update(self, id: int, **kwargs) -> Optional[T]:
        """Обновляет свойства объекта по его идентификатору."""
        ...

    @abstractmethod
    async def delete(self, id: int) -> None:
        """Удаляет объект по его идентификатору."""
        ...  # Предполагается, что репозиторий уже реализован


class IUnitOfWork(ABC):
    events: IRepository

    @abstractmethod
    async def __aenter__(self):
        """Асинхронная поддержка контекстного менеджера."""
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Асинхронная поддержка контекстного менеджера для выхода из блока."""
        ...

    @abstractmethod
    async def commit(self):
        """Подтверждение транзакции."""
        ...

    @abstractmethod
    async def rollback(self):
        """Откат транзакции."""
        ...
