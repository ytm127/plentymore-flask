import os
basedir = os.path.abspath(os.path.dirname(__file__))

# use a class to keep all the configuraiton information organized 

# change the non environement password laster 
# understand that the SECRET_KEY is an environment variable 
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False