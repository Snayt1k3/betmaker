from typing import List

from fastapi import APIRouter, Depends, HTTPException

from src.application.dto.bet import BetCreate, BetRead
from src.application.dto.event import EventDTO
from src.application.enum import EventStatus
from src.application.services.bet import BetService
from src.application.services.event import EventService
from src.ioc import IoC

router = APIRouter()

ioc = IoC()


@router.post("/", response_model=BetRead)
async def create_bet(
        bet_data: BetCreate,
        bet_service: BetService = Depends(ioc.bet_service)
):
    """
    Создает новую ставку на событие.
    """
    try:
        return await bet_service.create_bet(bet_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[BetRead])
async def get_all_bets(
        bet_service: BetService = Depends(ioc.bet_service)
):
    """
    Возвращает список всех сделанных ставок.
    """
    return await bet_service.get_all_bets()


@router.get("/event/active", response_model=List[EventDTO])
async def get_active_events(
        event_service: EventService = Depends(ioc.event_service)
):
    """
    Возвращает список всех ивентов доступных для ставки
    """
    return await event_service.get_active_events()


@router.patch("/event/{event_id}", response_model=List[BetRead])
async def update_bets_status(
        event_id: int,
        status: EventStatus,
        bet_service: BetService = Depends(ioc.bet_service)
):
    """
    Обновляет статус ставки.
    """

    return await bet_service.update_bets_by_event(event_id, status)
