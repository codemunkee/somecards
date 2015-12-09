from flask import render_template, flash, redirect
from somecards import app, models, db
from .forms import AddCardForm, RemoveCardForm


@app.route('/')
def index():
    cards = models.Card.query.all()
    return render_template('index.html',
                           cards=cards)


@app.route('/add/<int:category_id>', methods=['GET', 'POST'])
def add_to_category():

    form = AddCardForm()

    if form.validate_on_submit():
        new_card = models.Card(form.question.data, form.answer.data)
        db.session.add(new_card)
        db.session.commit()
        flash('New Card Added, Question: %s' % form.question.data)
        return redirect('/add')

    return render_template('add.html',
                           form=form)


@app.route('/add', methods=['GET'])
def add():

    print 'We need a category'
    categories = models.Category.query.all()
    return render_template('add.html', categories=categories)


@app.route('/review')
def review():
    cards = models.Card.query.all()
    return render_template('review.html', cards=cards)


@app.route('/remove', methods=['GET', 'POST'])
def remove():
    cards = [(card.id, card.question) for card in models.Card.query.all()]
    form = RemoveCardForm()
    form.card.choices = cards
    if form.is_submitted():
        models.Card.query.filter_by(id=form.card.data).delete()
        db.session.commit()
        flash('Card (id:%s) Removed.' % form.card.data)
        return redirect('/remove')

    return render_template('remove.html',
                           form=form)




