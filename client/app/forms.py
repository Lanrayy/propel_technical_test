from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import InputRequired

class AddContactForm(FlaskForm):
    first_name = StringField('first_name', validators=[InputRequired()])
    last_name = StringField('last_name', validators=[InputRequired()])
    phone = StringField('phone', validators=[InputRequired()])
    email = EmailField('email', validators=[InputRequired()])