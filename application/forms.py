from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username=StringField('Username', validators=[
        DataRequired(),
        Length(min=2,max=20)
    ])
    first_name = StringField('First Name')
    surname = StringField('Surname')
    date_of_birth = DateField('Date of Birth')
    submit = SubmitField('Submit')

class RecordForm(FlaskForm):
    exercise_name=SelectField('Exercise', choices=[])
    personal_best=DecimalField('Enter your personal best', places=1)
    submit = SubmitField('Submit')

class ExerciseForm(FlaskForm):
    exercise_name=SelectField('Exercise', choices=[])
    submit = SubmitField('Submit')