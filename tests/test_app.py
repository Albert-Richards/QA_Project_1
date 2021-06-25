from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Exercises
from application.routes import exercise

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
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
    
    def tearDown(self):

        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code, 200)
    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code, 200)

class TestFunc(TestBase):
    def test_exercise(self):
        self.assertEqual(exercise(1), 'Deadlift')
        self.assertEqual(exercise(2), 'Squat')
        self.assertEqual(exercise(3), 'Bench press')
        self.assertEqual(exercise(4), 'Overhead press')