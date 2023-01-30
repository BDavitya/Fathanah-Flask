from app import db

def checkUser(a):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM `admin-data` WHERE email=%s", (a,))
    a = cur.fetchone()
    return a