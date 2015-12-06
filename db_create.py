#!flask/bin/python

# A small script to create our database
from config import SQLALCHEMY_DATABASE_URI

from somecards import db, models

db.create_all()

# add a couple cards off the bat

card1 = models.Card('How many miles to the moon?', '239 thousand')
card2 = models.Card('How many miles to the sun?', '93 million')

db.session.add(card1)
db.session.add(card2)

db.session.commit()
