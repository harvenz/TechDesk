import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

def init_db():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ticket (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
