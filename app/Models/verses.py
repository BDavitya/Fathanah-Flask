from app import db
def versesDatas():
    cur = db.connection.cursor()
    cur.execute("SELECT `quran-data`.`id`, `quran-surah`.`name`, `quran-data`.`arab`, `quran-data`.`latin`, `quran-data`.`meaning` FROM `quran-data` INNER JOIN `quran-surah` ON `quran-data`.`surah`=`quran-surah`.`id`")
    b = cur.fetchall()
    return b

def versesUpdating(arab, latin, meaning, where):
    cur = db.connection.cursor()
    cur.execute("UPDATE `quran-data` SET `arab`=%s, `latin`=%s, `meaning`=%s WHERE id=%s", (arab, latin, meaning, where))
    db.connection.commit()