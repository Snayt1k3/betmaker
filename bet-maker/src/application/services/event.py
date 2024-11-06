from typing import List

from src.adapters.request import HttpClient
from src.application.dto.event import EventDTO
from src.config import http_config


class EventService:
    def __init__(self, request: HttpClient) -> None:
        self.request = request

    async def get_active_events(self) -> List[EventDTO]:
        events = await self.request.get(http_config.URL_GET_ACTIVE_EVENTS)
        return events
