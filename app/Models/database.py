from app import db

class aboutData(db.Model):
    __tablename__ = 'about-data'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    img = db.Column(db.Integer(), db.ForeignKey("img-asset.id"), unique=True)
    desc = db.Column(db.String(4294000000))

class adminData(db.Model):
    __tablename__ = 'admin-data'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    role = db.Column(db.Integer(), db.ForeignKey("admin-role.id"), unique=True)
    instagram = db.Column(db.String(1000))
    img = db.Column(db.String(1000))
    path = db.Column(db.Integer(), db.ForeignKey("img-path.id"), unique=True)

class adminRole(db.Model):
    __tablename__ = 'admin-role'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    role = db.Column(db.String(20))
    role_adminData = db.relationship('adminData', backref='admin-role')

class articleCategory(db.Model):
    __tablename__ = 'article-category'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    category = db.Column(db.String(40))
    category_articleData = db.relationship('articleData', backref='article-category')

class articleData(db.Model):
    __tablename__ = 'article-data'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.datetim)
    email = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    role = db.Column(db.Integer(), db.ForeignKey("admin-role.id"), unique=True)
    instagram = db.Column(db.String(1000))
    img = db.Column(db.String(1000))
    path = db.Column(db.Integer(), db.ForeignKey("img-path.id"), unique=True)

class imgAsset(db.Model):
    __tablename__ = 'img-asset'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    img = db.Column(db.String(40))
    path = db.Column(db.Integer(), db.ForeignKey("img-path.id"), unique=True)
    img_aboutData = db.relationship('aboutData', backref='img-asset')

class imgPath(db.Model):
    __tablename__ = 'img-path'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    path = db.Column(db.String(40))
    path_imgAsset = db.relationship('imgAsset', backref='img-path')
    path_adminData = db.relationship('adminData', backref='img-path')