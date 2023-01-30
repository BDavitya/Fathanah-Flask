from app import db
def updateData(name, email, ig, img, where):
    cur = db.connection.cursor()
    cur.execute("UPDATE `admin-data` SET name=%s, email=%s, instagram=%s, image=%s WHERE id=%s", (name, email, ig, img, where))
    db.connection.commit()

def updatePasswords(password, where):
    cur = db.connection.cursor()
    cur.execute("UPDATE `admin-data` SET password=%s WHERE name=%s", (password, where))
    db.connection.commit()