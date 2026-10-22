import sqlite3

conn = sqlite3.connect("test.db")

def init_db():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ticket (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

def get_tickets():
    cursor = conn.execute("SELECT * FROM ticket")
    tickets = cursor.fetchall()
    return tickets

def create_tickets(subject: str, message: str):
    cursor = conn.execute("""
        INSERT INTO ticket (subject, message)
        VALUES (?, ?)
    """, (subject, message))

    conn.commit()

    ticket_id = cursor.lastrowid
    return ticket_id