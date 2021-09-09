import sqlite3

DATABASE_NAME = "whorules.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS beers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                defendant TEXT NOT NULL,
                defendant_id INTEGER NOT NULL,
                prosecutors TEXT NOT NULL,
				description TEXT NOT NULL,
				count INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
