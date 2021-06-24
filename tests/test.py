from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from app import app, db
from app.models import Exercises, User_stats

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all()

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):
    TEST_CASES = 'Chess', 'Backgammon', 'Hungry Hungry Hippos', '#@!%$', ';DROP TABLE games;', 'Borderlands 3'

    def submit_input(self, case): 
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
        for case in self.TEST_CASES:
            self.submit_input(case)
            self.assertIn(url_for('home'), self.driver.current_url)

            text = self.driver.find_element_by_xpath('/html/body/ul/li[1]').text #
            self.assertEqual(text, case)

            entry = Games.query.filter_by(name=case).first()
            self.assertNotEqual(entry, None)


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

