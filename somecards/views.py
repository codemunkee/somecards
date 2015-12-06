from flask import render_template, flash, redirect
from somecards import app, models
from .forms import CardForm


@app.route('/')
def index():
    cards = models.Card.query.all()
    return render_template("index.html",
                           cards=cards)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CardForm()
    if form.validate_on_submit():
        flash('New Card Added!')
        return redirect('/add')

    return render_template('add.html',
                           form=form)