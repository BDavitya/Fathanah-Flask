from flask import Flask, session
from flask_ckeditor import CKEditor
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fathanah'
db = MySQL(app)
app.secret_key = "012#!ApAAjaBoleh)(*^%"

app.config['CKEDITOR_HEIGHT'] = '500'
app.config['CKEDITOR_WIDTH'] = '1000'
app.config['CKEDITOR_PKG_TYPE'] = 'full'
ckeditor = CKEditor(app)

from app.Controllers import log, home, about, ahusna, quran

from datetime import timedelta
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)