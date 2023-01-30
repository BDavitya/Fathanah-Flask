from app import db
def aboutDatas():
    cur = db.connection.cursor()
    cur.execute("SELECT `about-data`.`id`, `about-data`.`name`, `img-asset`.`img`, `about-data`.`desc`, `img-path`.`path` FROM `about-data` INNER JOIN `img-asset` ON `about-data`.`img`=`img-asset`.`id` INNER JOIN `img-path` ON `img-asset`.`path`=`img-path`.`id`")
    b = cur.fetchall()
    return b

def aboutUpdate(a):
    cur = db.connection.cursor()
    cur.execute("SELECT `about-data`.`id`, `about-data`.`name`, `img-asset`.`img`, `about-data`.`desc`, `img-path`.`path` FROM `about-data` INNER JOIN `img-asset` ON `about-data`.`img`=`img-asset`.`id` INNER JOIN `img-path` ON `img-asset`.`path`=`img-path`.`id` WHERE `about-data`.`name`=%s", (a,))
    b = cur.fetchone()
    return b

def aboutUpdating(image, desc, where):
    cur = db.connection.cursor()
    cur.execute("UPDATE `about-data` INNER JOIN `img-asset` ON `about-data`.`img`=`img-asset`.`id` SET `img-asset`.`img` = %s, `about-data`.`desc` = %s  WHERE `about-data`.`name` = %s", (image, desc, where))
    db.connection.commit()