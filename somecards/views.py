from flask import render_template, flash, redirect
from somecards import app, models


@app.route('/')
def index():
    cards = models.Card.query.all()
    return render_template("index.html",
                           cards=cards)

@app.route('/add')
def add():
    return render_template("add.html")