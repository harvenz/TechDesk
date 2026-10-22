import app.database as db

class TicketService:
    def __init__(self):
        pass

    def get(self):
        return db.get_tickets()

    def create(self, subject: str, message: str):
        return db.create_tickets(subject, message)