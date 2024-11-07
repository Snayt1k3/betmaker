from datetime import datetime
from typing import List, Optional

from config import http_config
from src.adapters.request import HttpClient
from src.adapters.storage.models import Event, EventStatus
from src.application.interface import IUnitOfWork


class EventService:
    def __init__(self, uow: IUnitOfWork, request: HttpClient) -> None:
        self.uow = uow
        self.request = request

    async def create_event(self, odds: float, deadline: int) -> Event:
        """Создает новое событие."""
        async with self.uow as uow:
            event = await uow.events.add(
                odds=odds, deadline=datetime.fromtimestamp(deadline), status=EventStatus.UNFINISHED
            )
        return event

    async def get_event_by_id(self, id: int) -> Optional[Event]:
        """Получает событие по идентификатору."""
        async with self.uow as uow:
            return await uow.events.get_by_id(id)

    async def update_event_status(
            self, id: int, new_status: EventStatus
    ) -> Optional[Event]:
        """Обновляет статус события."""
        async with self.uow as uow:
            event = await uow.events.update(id, status=new_status)
        return event

    async def delete_event(self, id: int) -> None:
        """Удаляет событие по идентификатору."""
        async with self.uow as uow:
            await uow.events.delete(id)

    async def filter_events(self, **kwargs) -> List[Event]:
        """Фильтрует события по заданным критериям."""
        async with self.uow as uow:
            return await uow.events.filter_by(**kwargs)

    async def get_active_events(self) -> List[Event]:
        async with self.uow as uow:
            return await uow.events.filter_by(status=EventStatus.UNFINISHED)

    async def update_bets(self, status: EventStatus, event_id: int) -> None:
        await self.request.patch(http_config.URL_UPDATE_BETS + str(event_id), json={"status": status.value})
