from fastapi import FastAPI
from app.routes.ticket import router as ticket_router

app = FastAPI()

app.include_router(ticket_router, prefix="/ticket")