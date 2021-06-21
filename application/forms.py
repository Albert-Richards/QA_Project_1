from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ""

class RegisterForm(FlaskForm):
    username=StringField('Username:')
    first_name = StringField('First Name:')
    surname = StringField('Surname:')
    

