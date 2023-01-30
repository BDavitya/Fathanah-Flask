from app import db
def quranDatas():
    cur = db.connection.cursor()
    cur.execute("SELECT `quran-surah`.`id`, `quran-surah`.`name`, `quran-surah`.`meaning`, COUNT(`quran-data`.`surah`) AS verses FROM `quran-data` INNER JOIN `quran-surah` ON `quran-data`.`surah`=`quran-surah`.id GROUP BY `quran-data`.`surah` ORDER BY `quran-surah`.id ASC")
    a = cur.fetchall()
    return a

def quranUpdating(name, meaning, where):
    cur = db.connection.cursor()
    cur.execute("UPDATE `quran-surah` SET `name`=%s, `meaning`=%s WHERE id=%s", (name, meaning, where))
    db.connection.commit()

def surahDatas(a):
    cur = db.connection.cursor()
    cur.execute("SELECT `quran-data`.`id`, `quran-surah`.`name`, `quran-data`.`arab`, `quran-data`.`latin`, `quran-data`.`meaning` FROM `quran-data` INNER JOIN `quran-surah` ON `quran-data`.`surah`=`quran-surah`.`id` WHERE `quran-surah`.`name` = %s", (a,))
    b = cur.fetchall()
    return b

def surahUpdating(arab, latin, meaning, where):
    cur = db.connection.cursor()
    cur.execute("UPDATE `quran-data` SET `arab`=%s, `latin`=%s, `meaning`=%s WHERE id=%s", (arab, latin, meaning, where))
    db.connection.commit()