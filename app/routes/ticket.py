from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_tickets():
    return {"Hello": "World"}


@router.post("/create")
async def create_ticket(subject: str, message: str):
    return {"subject": subject, "message": message}