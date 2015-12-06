from flask import render_template, flash, redirect
from somecards import app, models, db
from .forms import CardForm


@app.route('/')
def index():
    cards = models.Card.query.all()
    return render_template('index.html',
                           cards=cards)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = CardForm()
    if form.validate_on_submit():
        new_card = models.Card(form.question.data, form.answer.data)
        db.session.add(new_card)
        db.session.commit()
        flash('New Card Added, Question: %s' % form.question.data)
        return redirect('/add')

    return render_template('add.html',
                           form=form)

