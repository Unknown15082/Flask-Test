import os

cwddir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(cwddir, 'flasktest.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False