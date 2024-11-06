from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi import Depends, HTTPException

from src.adapters.storage.models import EventStatus
from src.application.dto import EventDTO
from src.application.services.event import EventService
from src.ioc import IoC

events_router = APIRouter()
ioc = IoC()


@events_router.post("/", response_model=EventDTO)
async def create_event(
    odds: float,
    deadline: datetime,
    event_service: EventService = Depends(ioc.event_service),
):
    try:
        event = await event_service.create_event(odds, deadline)
        return event
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@events_router.get("/{id}", response_model=EventDTO)
async def get_event(id: int, event_service: EventService = Depends(ioc.event_service)):
    event = await event_service.get_event_by_id(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@events_router.get("/active", response_model=List[EventDTO])
async def get_active_events(event_service: EventService = Depends(ioc.event_service)):
    events = await event_service.get_active_events()
    return events


@events_router.patch("/{id}", response_model=EventDTO)
async def update_event_status(
    id: int,
    new_status: EventStatus,
    event_service: EventService = Depends(ioc.event_service),
):
    try:

        event = await event_service.update_event_status(id, new_status)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid status value")


@events_router.delete("/{id}", status_code=204)
async def delete_event(
    id: int, event_service: EventService = Depends(ioc.event_service)
):
    success = await event_service.delete_event(id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted successfully"}
