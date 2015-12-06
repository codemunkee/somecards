from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Reads our configuration options from config.py
app.config.from_object('config')

db = SQLAlchemy(app)

from somecards import views

