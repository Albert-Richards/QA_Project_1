from flask import redirect, url_for, render_template, request

from application import app, db
from application.models import Exercises, User_stats
from application.forms import RecordForm, ExerciseForm

@app.route('/')
def home():
    form = RecordForm(request.form)
       
    return render_template('update.html', form=form)

@app.route('/add', methods=['POST'])
def add():
    form = RecordForm(request.form)

    if form.validate_on_submit():
        db.session.add(User_stats(exercise_id=form.exercise_name.data,
        personal_best=form.personal_best.data)
        db.session.commit()
    redirect(url_for('home'))

@app.route('/delete', methods=['DELETE'])
def delete():
    form = ExerciseForm(request.form)

    if form.validate_on_submit():
        db.session.delete(User_stats(exercise_id=form.exercise_name.data)
        db.session.commit()
    return redirect(url_for('index', error=error))

 
    