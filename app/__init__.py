from flask import Flask, session
from flask_ckeditor import CKEditor
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://fathanah:FathanahS3cr3t@157.245.207.179:5432/fathanah'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
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