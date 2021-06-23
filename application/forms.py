from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length
from application.models import Exercises

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
    exercises = Exercises.query.all()
    exercise_name=SelectField('Exercise', choices=[
        (exercises[0].id, exercises[0].exercise_name),
        (exercises[1].id, exercises[1].exercise_name),
        (exercises[2].id, exercises[2].exercise_name),
        (exercises[3].id, exercises[3].exercise_name)
        ])
    personal_best=DecimalField('Enter your personal best', places=1)
    submit = SubmitField('Submit')

"""class ExerciseForm(FlaskForm):
    exercises = Exercises.query.all()
    exercise_name=SelectField('Exercise' choices=[
        (exercises[0].id, exercises[0].exercise_name),
        (exercises[1].id, exercises[1].exercise_name),
        (exercises[2].id, exercises[2].exercise_name),
        (exercises[3].id, exercises[3].exercise_name)
        ])
    submit = SubmitField('Submit')"""