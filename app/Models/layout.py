from app import db
def iconNlogo():
    x = []
    cur = db.connection.cursor()
    cur.execute("SELECT `img-asset`.id, `img-asset`.name, `img-asset`.img, `img-path`.path FROM `img-asset` INNER JOIN `img-path` ON `img-asset`.path=`img-path`.id WHERE `img-asset`.name = 'dashboard'")
    a = cur.fetchone()
    x.append(a)
    cur.execute("SELECT `img-asset`.id, `img-asset`.name, `img-asset`.img, `img-path`.path FROM `img-asset` INNER JOIN `img-path` ON `img-asset`.path=`img-path`.id WHERE `img-asset`.name = 'favicon'")
    b = cur.fetchone()
    x.append(b)
    return x

def userData(a):
    cur = db.connection.cursor()
    cur.execute("SELECT `admin-data`.`id`, `admin-data`.`name`, `admin-data`.`email`, `admin-data`.`password`, `admin-role`.`role`, `admin-data`.`instagram`, `admin-data`.`image`, `img-path`.`path`  FROM `admin-data` INNER JOIN `admin-role` ON `admin-data`.`role`= `admin-role`.`id`INNER JOIN `img-path` ON `admin-data`.`path`=`img-path`.`id` WHERE `admin-data`.`id`=%s", (a,))
    b = cur.fetchone()
    return b

def aboutData():
    cur = db.connection.cursor()
    cur.execute("SELECT `about-data`.`id`, `about-data`.`name`, `img-asset`.`img`, `about-data`.`desc`, `img-path`.`path` FROM `about-data` INNER JOIN `img-asset` ON `about-data`.`img`=`img-asset`.`id` INNER JOIN `img-path` ON `img-asset`.`path`=`img-path`.`id`")
    b = cur.fetchall()
    return b