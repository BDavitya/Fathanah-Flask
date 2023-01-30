import hashlib
from types import NoneType
from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.Models.log import checkUser
from app.Models.layout import iconNlogo
from app.Controllers.home import *

@app.route('/')
def admin():
    if 'id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.errorhandler(404)
def pageNotFound(e):
    logoNicon = iconNlogo()
    return render_template('log/error.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], id = "404"), 404

@app.route('/error-session')
def notInSession():
    logoNicon = iconNlogo()
    return render_template('log/error.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], id = "419")

@app.route('/assalamualaikum', methods=['GET','POST'])
def login():
    logoNicon = iconNlogo()
    if request.method == "POST":
        email = request.form.get("email")
        pwd = request.form.get("password") 
        user = checkUser(email)
        if type(user) != NoneType:
            if email == user[2]:
                b = pwd.encode('utf-8')
                hash_object = hashlib.sha256(b)
                hex_dig = hash_object.hexdigest()
                if user[3] == hex_dig:    
                    if user[4] == 2:
                        session['id'] = user[0]
                        flash('Welcome ' + user[1] + '! You are logedin now!')
                        return redirect(url_for('admin'))
                    else:
                        flash('ERROR : Account not belong here')
                else:
                    flash('ERROR : Wrong password')
            else:
                flash('ERROR : This email is not used yet')
        else:
            flash('ERROR : This email is not used yet')
    return render_template('log/login.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], title="Login Page")

@app.route("/waalaikumsalam")
def logout():
    session.clear()
    flash('End Session Success')
    return redirect(url_for('login'))