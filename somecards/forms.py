from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class AddCardForm(Form):
    question = StringField('question', validators=[DataRequired()])
    answer = StringField('answer', validators=[DataRequired()])


class RemoveCardForm(Form):
    #card = SelectField(choices=[(card.id, card.question) for card in models.Card.query.all()])
    card = SelectField(choices=[])
