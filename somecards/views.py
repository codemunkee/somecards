from flask import render_template, flash, redirect, session, request, url_for
from somecards import app, models, db
from .forms import AddCardForm, RemoveCardForm, ReviewForm


@app.route('/')
def index():
    categories = models.Category.query.all()
    return render_template('index.html',
                           categories=categories)


@app.route('/add/<int:category_id>', methods=['GET', 'POST'])
def add_to_category(category_id):

    form = AddCardForm()

    if form.validate_on_submit():
        new_card = models.Card(form.question.data, form.answer.data, category_id)
        db.session.add(new_card)
        db.session.commit()
        flash('New Card Added, Question: %s' % form.question.data)
        return redirect('/add/%s' % category_id)

    return render_template('add.html',
                           form=form)


@app.route('/add', methods=['GET'])
def add():
    categories = models.Category.query.all()
    return render_template('add.html', categories=categories)


@app.route('/review')
def review():
    categories = models.Category.query.all()
    return render_template('review.html', categories=categories)


@app.route('/review/<int:category_id>', methods=['GET', 'POST'])
def review_category(category_id):

    form = ReviewForm()

    # Get our cards for the specific category
    cards = [(card.id, card.question, card.answer)
             for card in models.Card.query.filter_by(category_id=category_id)]

    # We have a dictionary to keep track of what card we were last on when
    # we do reviews of a set of cards (a category). So, we make a dictionary
    # here to hold this information if it doesn't already exist.
    if not session.get('review'):
        session['review'] = {}

    # If there is not a sub dictionary for a specific category ID, we create it
    # and set the index of the first card to 0.
    if not session['review'].get(str(category_id)):
        session['review'][str(category_id)] = {}
        session['review'][str(category_id)]['current_index'] = 0

    # If we get a form submission, increment the card number, if the number
    # we increment to is larger than the number of cards we have then present
    # the results.
    if form.validate_on_submit():
        session['review'][str(category_id)]['current_index'] += 1
        if session['review'][str(category_id)]['current_index'] >= len(cards):
            flash('All questions complete!')
            print 'flashed!'
            session['review'][str(category_id)]['current_index'] = 0

    # Get our current id, question, and answer for sending to the template
    card_index = session['review'][str(category_id)]['current_index']
    card.id = cards[card_index][0]
    card.question = cards[card_index][1]
    card.answer = cards[card_index][2]

    return render_template('review.html', card=card, card_num=card_index + 1,
                           total_questions=len(cards), form=form)


@app.route('/remove/<int:category_id>', methods=['GET', 'POST'])
def remove_from_category(category_id):
    cards = [(card.id, card.question)
             for card in models.Card.query.filter_by(category_id=category_id)]
    form = RemoveCardForm()
    form.card.choices = cards
    if form.is_submitted():
        models.Card.query.filter_by(id=form.card.data).delete()
        db.session.commit()
        flash('Card (id:%s) Removed.' % form.card.data)
        return redirect('/remove')

    return render_template('remove.html',
                           form=form)


@app.route('/remove', methods=['GET', 'POST'])
def remove():
    categories = models.Category.query.all()
    return render_template('remove.html',
                           categories=categories)