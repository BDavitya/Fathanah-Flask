from wtforms import Form, StringField, PasswordField, validators

class profileUpdate(Form):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Used Email', [validators.DataRequired()])
    role = StringField('Role / Position', [validators.DataRequired()])
    instagram = StringField('Instagram Account', [validators.DataRequired()])

class passwordUpdate(Form):
    oldPassword = PasswordField('Old Password', [validators.DataRequired()])
    newPassword = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirmNewPassword', message='Passwords must match', )
    ])
    confirmNewPassword = PasswordField('Repeat Password',  [validators.DataRequired()])