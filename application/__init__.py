from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=getenv('URI_project_db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']=getenv('S_key')

db = SQLAlchemy(app)

from application import routes