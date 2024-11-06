from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.adapters.storage.models import Event
from src.application.interface import IRepository


class EventRepository(IRepository[Event]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, **kwargs) -> Event:
        """Создает новое событие и сохраняет его в базе данных."""
        new_event = Event(
            id=None,
            **kwargs
        )
        self.session.add(new_event)
        return new_event

    async def get_by_id(self, id: int) -> Optional[Event]:
        """Возвращает событие по его идентификатору."""
        result = await self.session.execute(select(Event).where(Event.id == id))
        return result.scalars().first()

    async def filter_by(self, **kwargs) -> List[Event]:
        result = await self.session.execute(
            select(Event).filter_by(**kwargs)
        )
        return result.scalars().all()

    async def update(self, id: str, **kwargs) -> Optional[Event]:
        """Обновляет статус события по его идентификатору."""
        query = (
            update(Event)
            .where(Event.id == id)
            .values(**kwargs)
            .returning(Event)
        )
        res = await self.session.execute(query)

        return res.first()

    async def delete(self, id: int) -> None:
        """Удаляет событие по его идентификатору."""
        event = await self.get_by_id(id)

        if event:
            await self.session.delete(event)
