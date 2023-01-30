from wtforms import Form, StringField, validators, HiddenField

class quranForm(Form):
    id = HiddenField('', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired()])
    meaning = StringField('Meaning', [validators.DataRequired()])

class surahForm(Form):
    id = HiddenField('', [validators.DataRequired()])
    arab = StringField('Arab', [validators.DataRequired()])
    latin = StringField('Latin', [validators.DataRequired()])
    meaning = StringField('Meaning', [validators.DataRequired()])