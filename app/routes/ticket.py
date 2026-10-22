from fastapi import APIRouter
from app.services.ticket import TicketService

router = APIRouter()
ticket = TicketService()

@router.get("/")
async def get_tickets():
    tickets = ticket.get()
    return tickets


@router.post("/create")
async def create_ticket(subject: str, message: str):
    result = ticket.create(subject, message)
    return result