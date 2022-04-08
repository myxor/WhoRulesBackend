from db import get_db
from datetime import datetime


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        # col[0] is the column name
        d[col[0]] = row[idx]
    return d


def get_beers():
    db = get_db()
    db.row_factory = dict_factory
    cursor = db.cursor()
    query = "SELECT id, date, defendant, defendant_id, prosecutors, description, count FROM beers"
    cursor.execute(query)
    data = cursor.fetchall()
    return data



def insert_beer(date, defendant, defendant_id, prosecutors, description, count):
    if date is None:
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
    if defendant_id is None or int(defendant_id) < 0:
        defendant_id = "0"
    if prosecutors is None:
        prosecutors = ""
    if description is None:
        description = ""
    if count is None or int(count) < 1:
        count = "1"

    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO beers(date, defendant, defendant_id, prosecutors, description, count) VALUES " \
                "(?, ?, ?, ?, ?, ?) "
    cursor.execute(statement, [date, defendant, defendant_id, prosecutors, description, count])
    db.commit()
    return True


def update_beer(id, date, defendant, defendant_id, prosecutors, description, count):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE beers SET date = ?, defendant = ?, defendant_id = ?, prosecutors = ?, description = ?, " \
                "count WHERE id = ?"
    cursor.execute(statement, [date, defendant, defendant_id, prosecutors, description, count, id])
    db.commit()
    return True


def delete_beer(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM beers WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True
