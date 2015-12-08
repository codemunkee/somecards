from flask import render_template, flash, redirect, request
from somecards import app, models, db
from .forms import AddCardForm, RemoveCardForm


@app.route('/')
def index():
    cards = models.Card.query.all()
    return render_template('index.html',
                           cards=cards)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddCardForm()

    if form.validate_on_submit():
        new_card = models.Card(form.question.data, form.answer.data)
        db.session.add(new_card)
        db.session.commit()
        flash('New Card Added, Question: %s' % form.question.data)
        return redirect('/add')

    return render_template('add.html',
                           form=form)


@app.route('/remove', methods=['GET', 'POST'])
def remove():
    form = RemoveCardForm()
    if form.is_submitted():
        models.Card.query.filter_by(id=form.card.data).delete()
        db.session.commit()
        flash('Card (id:%s) Removed.' % form.card.data)
        return redirect('/remove')

    return render_template('remove.html',
                           form=form)


