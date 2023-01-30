from app import db

def manyArticle():
    cur = db.connection.cursor()
    cur.execute("SELECT id FROM `article-data`")
    a = cur.fetchall()
    return len(a)

def manyUser():
    cur = db.connection.cursor()
    cur.execute("SELECT id FROM `web-user-data`")
    a = cur.fetchall()
    return len(a)

def manyPray():
    cur = db.connection.cursor()
    cur.execute("SELECT id FROM `pray-data`")
    a = cur.fetchall()
    return len(a)

def manyStory():
    cur = db.connection.cursor()
    cur.execute("SELECT no FROM `diary-data`")
    a = cur.fetchall()
    return len(a)

def usingDiary():
    cur = db.connection.cursor()
    cur.execute("SELECT DISTINCT user FROM `diary-data`")
    a = cur.fetchall()
    return len(a)