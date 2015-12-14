from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class AddCardForm(Form):
    question = StringField('question', validators=[DataRequired()])
    answer = StringField('answer', validators=[DataRequired()])


class RemoveCardForm(Form):
    card = SelectField(choices=[])


# We use this to see if the user knows or doesn't know the card being presented
class ReviewForm(Form):
    yes = SubmitField('yes')
    no = SubmitField('no')
