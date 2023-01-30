from wtforms import Form, StringField, validators, HiddenField

class ahusnaForm(Form):
    id = HiddenField('', [validators.DataRequired()])
    arab = StringField('Arab', [validators.DataRequired()])
    latin = StringField('Latin', [validators.DataRequired()])
    meaning = StringField('Meaning', [validators.DataRequired()])