import hashlib
import os
from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.Models.index import manyArticle, manyUser, manyPray, manyStory, usingDiary
from app.Models.layout import iconNlogo, userData, aboutData
from app.Models.profile import updateData, updatePasswords
from app.Controllers.log import *
from app.Forms.profile import profileUpdate, passwordUpdate
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/byfmn')
def home():
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        article = manyArticle()
        user = manyUser()
        pray = manyPray()
        story = manyStory()
        diary = usingDiary()
        about = aboutData()
        return render_template('home/index.html', article = article, user = user, pray = pray, story = story, diary = diary, brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, about=about)
    return redirect(url_for('notInSession'))

@app.route('/nafsi-ana', methods=['POST', 'GET'])
def updateProfile():
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        form = profileUpdate(request.form)
        if request.method == "POST":
            UPLOAD_FOLDER = 'static\\admin-pp'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            name = form.name.data
            email = form.email.data
            instagram = form.instagram.data
            pic = request.files['pic']
            filename = pic.filename
            if filename == '':
                filename = dataUser[6]
            else:
                if allowed_file(filename):
                    filename = secure_filename(filename)
                    pic.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))  
                else:
                    flash('JPG, PNG, and JPEG type only!')
                    return redirect(url_for('updateProfile'))
            updateData(name, email, instagram, filename, session['id'])
            flash('Profile Data Already Updated')
            return redirect(url_for('home'))
        return render_template('home/profileUpdate.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, form = form, about=about)
    return redirect(url_for('notInSession'))

@app.route('/nafsi-ana-pwd', methods=['POST', 'GET'])
def updatePassword():
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        form = passwordUpdate(request.form)
        if request.method == "POST":
            old = form.oldPassword.data
            new = form.newPassword.data
            repeat = form.confirmNewPassword.data
            hash_old = hashlib.sha256(old.encode('utf-8'))
            hex_old = hash_old.hexdigest()
            if dataUser[3] == hex_old:    
                if len(new) >=8:
                    if new == repeat:
                        hash_new = hashlib.sha256(new.encode('utf-8'))
                        hex_new = hash_new.hexdigest()
                        updatePasswords(hex_new, dataUser[1])
                        flash('Password Already Updated')
                        return redirect(url_for('updateProfile'))
                    else:
                        flash('ERROR : New Password and Confirm New Password must be match')
                        return redirect(url_for('updatePassword'))
                else:
                    flash('ERROR : Length of New Password is less than allowable minimun of 8')
                    return redirect(url_for('updatePassword'))
            else:
                flash('ERROR : Wrong Input for Old Password')
                return redirect(url_for('updatePassword'))
        return render_template('home/passwordUpdate.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, form = form, about=about)
    return redirect(url_for('notInSession'))