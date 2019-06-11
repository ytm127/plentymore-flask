import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# use a class to keep all the configuraiton information organized 

# change the non environement password laster 
# understand that the SECRET_KEY is an environment variable 
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # loggin to stdout for heroku 
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')