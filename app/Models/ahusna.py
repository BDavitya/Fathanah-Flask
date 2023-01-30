from app import db
def ahusnaDatas():
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM `asmaul-husna-data`")
    b = cur.fetchall()
    return b

def ahusnaUpdating(arab, latin, meaning, where):
    cur = db.connection.cursor()
    cur.execute("UPDATE `asmaul-husna-data` SET `arab`=%s, `latin`=%s, `meaning`=%s WHERE id=%s", (arab, latin, meaning, where))
    db.connection.commit()