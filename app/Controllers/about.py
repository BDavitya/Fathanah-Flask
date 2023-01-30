import os
from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.Models.about import aboutDatas, aboutUpdate, aboutUpdating
from app.Models.layout import iconNlogo, userData, aboutData
from app.Controllers.log import *
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/us-tuoba')
def aboutDisplay():
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        datas = aboutDatas()
        return render_template('website/about.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, about=about, datas=datas, menu="website", submenu="about")
    return redirect(url_for('notInSession'))

@app.route('/us-tuoba/<string:name>', methods=['POST', 'GET'])
def aboutUpdates(name):
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        datas = aboutUpdate(name)
        if request.method == "POST":
            UPLOAD_FOLDER = 'static\\asset'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            pic = request.files['pic']
            filename = pic.filename
            if filename == '':
                filename = datas[2]
            else:
                if allowed_file(filename):
                    filename = secure_filename(filename)
                    pic.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))  
                else:
                    flash('JPG, PNG, and JPEG type only!')
                    return redirect(url_for('aboutUpdate'))
            description = request.form.get('ckeditor')
            aboutUpdating(filename, description, name)
            flash(name + ' Data Already Updated')
            return redirect(url_for('aboutDisplay'))
        return render_template('website/aboutUpdate.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, datas=datas, about=about,  menu="website", submenu="about")
    return redirect(url_for('notInSession'))