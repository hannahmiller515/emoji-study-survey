# app/survey/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, ValidationError
from wtforms.validators import InputRequired,DataRequired

from ..models import Survey

class ConsentForm(FlaskForm):
    """
    Form for users to consent or not
    """
    consent = RadioField(choices=Survey.informed_consent["options"],
                         validators=[InputRequired()])
    submit = SubmitField('Submit')
