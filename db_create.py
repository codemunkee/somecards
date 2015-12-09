#!flask/bin/python

# A small script to create our database
from config import SQLALCHEMY_DATABASE_URI

from somecards import db, models

db.create_all()

# add a couple cards off the bat

category1 = models.Category('Random')
category2 = models.Category('Docker')

db.session.add(category1)
db.session.add(category2)

category1.cards = [
    models.Card('How many miles to the moon?', '239 thousand'),
    models.Card('How many miles to the sun?', '93 million')]

db.session.add(category1)

db.session.commit()
