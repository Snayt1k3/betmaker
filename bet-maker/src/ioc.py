from contextlib import asynccontextmanager
from src.application.services.event import EventService
from src.application.services.bet import BetService

from src.adapters.uow import UnitOfWork
from src.adapters.request import HttpClient


class IoC:
    @asynccontextmanager
    async def event_service(self) -> EventService:
        uow = HttpClient()
        yield EventService(uow)

    @asynccontextmanager
    async def bet_service(self) -> BetService:
        uow = UnitOfWork()
        yield BetService(uow)
