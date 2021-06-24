from flask import redirect, url_for, render_template, request

from application import app, db
from application.models import Exercises, User_stats
from application.forms import RecordForm

@app.route('/')
def home():
    records = User_stats.query.all()
    return records

@app.route('/add', methods=['GET','POST'])
def add():
    form = RecordForm(request.form)
    exercises = Exercises.query.all()
    form.exercise_name.choices = [(exercises[0].id, exercises[0].exercise_name),
        (exercises[1].id, exercises[1].exercise_name),
        (exercises[2].id, exercises[2].exercise_name),
        (exercises[3].id, exercises[3].exercise_name)]
    if form.validate_on_submit():
        db.session.add(User_stats(exercise_id=form.exercise_name.data, personal_best=form.personal_best.data))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', form=form)

"""@app.route('/delete', methods=['DELETE'])
def delete():
    form = ExerciseForm(request.form)

    if form.validate_on_submit():
        db.session.delete(User_stats(exercise_id=form.exercise_name.data)
        db.session.commit()
    return redirect(url_for('index', error=error))"""

 
    