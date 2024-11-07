from typing import List

from fastapi import APIRouter, Depends, HTTPException

from src.application.dto.bet import BetCreate, BetRead
from src.application.dto.event import EventDTO
from src.application.enum import EventStatus
from src.application.services.bet import BetService
from src.application.services.event import EventService
from src.ioc import IoC

router = APIRouter()


@router.post("/", response_model=BetRead)
async def create_bet(bet_data: BetCreate, ioc: IoC = Depends(IoC)):
    """
    Создает новую ставку на событие.
    """
    try:
        async with ioc.bet_service() as bet_service:
            return await bet_service.create_bet(bet_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[BetRead])
async def get_all_bets(ioc: IoC = Depends(IoC)):
    """
    Возвращает список всех сделанных ставок.
    """
    async with ioc.bet_service() as bet_service:
        return await bet_service.get_all_bets()


@router.get("/event/active", response_model=List[EventDTO])
async def get_active_events(ioc: IoC = Depends(IoC)):
    """
    Возвращает список всех ивентов доступных для ставки
    """
    async with ioc.event_service() as event_service:
        return await event_service.get_active_events()


@router.patch("/event/update/{event_id}", response_model=List[BetRead])
async def update_bets_status(
    event_id: int, status: EventStatus, ioc: IoC = Depends(IoC)
):
    """
    Обновляет статус ставки.
    """
    async with ioc.bet_service() as bet_service:
        return await bet_service.update_bets_by_event(event_id, status)
