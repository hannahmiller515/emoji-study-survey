# app/survey/views.py

from flask import render_template

from . import survey
from ..models import Survey

@survey.route('/<survey_id>')
def landing_page(survey_id):
    """
    Render the informed consent template on the / route
    TODO capture url id!
    """
    Survey._survey_id = survey_id 
    return render_template('survey/index.html', informed_consent=Survey.informed_consent)

@survey.route('/1')
def page_one():
    """
    Render the page one template on the /page1 route
    """
    return render_template('survey/page1.html')