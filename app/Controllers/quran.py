from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.Models.quran import quranDatas, quranUpdating, surahDatas, surahUpdating
from app.Models.layout import iconNlogo, userData, aboutData
from app.Controllers.log import *
from app.Forms.quran import quranForm, surahForm

@app.route('/harus-alquran', methods=['POST', 'GET'])
def quranDisplay():
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        datas = quranDatas()
        form = quranForm(request.form)
        if request.method == "POST":
            id = form.id.data
            name = form.name.data
            meaning = form.meaning.data
            quranUpdating(name, meaning, id)
            flash(' Data Already Updated')
            return redirect(url_for('quranDisplay'))
        return render_template('website/quran.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, datas=datas, about=about,  menu="website", submenu="quran-surah", form=form)
    return redirect(url_for('notInSession'))

@app.route('/harus-alquran-<string:name>', methods=['POST', 'GET'])
def surahDisplay(name):
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        datas = surahDatas(name)
        form = surahForm(request.form)
        if request.method == "POST":
            id = form.id.data
            arab = form.arab.data
            latin = form.latin.data
            meaning = form.meaning.data
            surahUpdating(arab, latin, meaning, id)
            flash(' Data Already Updated')
            return redirect(url_for('surahDisplay', name=datas[0][1]))
        return render_template('website/surah.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, datas=datas, about=about,  menu="website", submenu="quran-surah", form=form,)
    return redirect(url_for('notInSession'))

