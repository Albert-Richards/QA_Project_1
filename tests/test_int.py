from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
import random

from application import app, db
from application.models import Exercises, User_stats

"""class TestBase(LiveServerTestCase):
    #TEST_PORT = 5050 

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            #LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

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

        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen('http://localhost:5000')
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):
    TEST_CASES = 100, 425.5, 12.001, 789, 47.753

    def submit_input(self, case):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="exercise_name"]').send_keys(random.randint(1,4))
        self.driver.find_element_by_xpath('//*[@id="personal_best"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
        for case in self.TEST_CASES:
            self.submit_input(case)
            self.assertIn(url_for('home'), self.driver.current_url)

            text = self.driver.find_element_by_xpath('/html/body/li').text 
            self.assertEqual(text, case)

            entry = User_stats.query.filter_by(personal_best=case).first()
            self.assertNotEqual(entry, None)"""