from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_login import LoginManager

# create an instance of flask
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app) # create a db instance to represent the database
migrate = Migrate(app, db) # create a migrate instance 
login = LoginManager(app) # create a login manager instance 
login.login_view = 'login'

from app import routes, models, errors
