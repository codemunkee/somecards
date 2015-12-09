from somecards import db


class Category(db.Model):
    __category__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    cards = db.relationship('Card', backref='category')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class Card(db.Model):
    __cards__ = 'cards'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question = db.Column(db.String(400), index=True, unique=False)
    answer = db.Column(db.String(600), index=False, unique=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return '<Question %r>' % self.question
