import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'somecards.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
