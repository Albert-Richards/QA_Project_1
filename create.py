from application import db
from application.models import Exercises

db.drop_all()
db.create_all()

ex_1 = Exercises(exercise_name= 'Deadlift')
ex_2 = Exercises(exercise_name = 'Squat')
ex_3 = Exercises(exercise_name = 'Bench press')
ex_4 = Exercises(exercise_name= 'Overhead press')

db.session.add(ex_1)
db.session.add(ex_2)
db.session.add(ex_3)
db.session.add(ex_4)
db.session.commit()