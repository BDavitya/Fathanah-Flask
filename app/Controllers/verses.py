from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.Models.verses import versesDatas, versesUpdating
from app.Models.layout import iconNlogo, userData, aboutData
from app.Controllers.log import *
from app.Forms.verses import versesForm

@app.route('/esrev-alquran', methods=['POST', 'GET'])
def versesDisplay():
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        datas = versesDatas()
        form = versesForm(request.form)
        if request.method == "POST":
            id = form.id.data
            arab = form.arab.data
            latin = form.latin.data
            meaning = form.meaning.data
            versesUpdating(arab, latin, meaning, id)
            flash(' Data Already Updated')
            return redirect(url_for('versesDisplay'))
        return render_template('website/verses.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, datas=datas, about=about,  menu="website", submenu="quran-verse", form=form)
    return redirect(url_for('notInSession'))

