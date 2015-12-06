from somecards import db


class Card(db.Model):
    __cards__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(400), index=True, unique=False)
    answer = db.Column(db.String(600), index=False, unique=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return '<Question %r>' % self.question