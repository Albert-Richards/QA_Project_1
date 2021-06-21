from application import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    first_name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    user_best = db.relationship('User_stats', backref='user')

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(20), nullable=False, unique=True)

class User_stats(db.Model):
    entry_no = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    personal_best = db.Column(db.Float(3,1), nullable=False, default=0.0)
 
