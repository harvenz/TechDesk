class TicketService:
    def __init__(self):
        pass

    def get(self):
        return {"Hello": "World"}

    def create(self, subject: str, message: str):
        return {"subject": subject, "message": message}