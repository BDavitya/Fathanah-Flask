from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.Models.ahusna import ahusnaDatas, ahusnaUpdating
from app.Models.layout import iconNlogo, userData, aboutData
from app.Controllers.log import *
from app.Forms.ahusna import ahusnaForm

@app.route('/ansuh-luamsa', methods=['POST', 'GET'])
def ahusnaDisplay():
    if 'id' in session:
        logoNicon = iconNlogo()
        dataUser = userData(session['id'])
        about = aboutData()
        datas = ahusnaDatas()
        form = ahusnaForm(request.form)
        if request.method == "POST":
            id = form.id.data
            arab = form.arab.data
            latin = form.latin.data
            meaning = form.meaning.data
            ahusnaUpdating(arab, latin, meaning, id)
            flash(' Data Already Updated')
            return redirect(url_for('ahusnaDisplay'))
        return render_template('website/ahusna.html', brand = logoNicon[0][2], path = logoNicon[0][3], icon = logoNicon[1][2], data = dataUser, datas=datas, about=about,  menu="website", submenu="asmaul-husna", form=form)
    return redirect(url_for('notInSession'))

