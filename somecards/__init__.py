from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)

# Reads our configuration options from config.py
app.config.from_object('config')

boostrap = Bootstrap(app)
db = SQLAlchemy(app)

from somecards import views

