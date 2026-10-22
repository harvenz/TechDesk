from fastapi import FastAPI
from app.database import init_db
from app.routes.ticket import router as ticket_router

init_db()
app = FastAPI()

app.include_router(ticket_router, prefix="/ticket")