from flask_wtf import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import InputRequired

class GenreForm(Form):
    genre = StringField('genre', validators=[InputRequired()])
