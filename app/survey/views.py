# app/survey/views.py

from flask import render_template
from flask import redirect

from . import survey
from ..models import Survey


# TODO uncomment!
"""
@survey.route('/')
def route_to_website():
    return redirect("http://z.umn.edu/emojistudy")
"""

    
@survey.route('/<survey_id>')
def landing_page(survey_id=None):
    """
    Render the informed consent template on the / route
    TODO capture url id!
    """
    if survey_id == None:
        Survey._survey_id = 1
    else:
        Survey._survey_id = survey_id
    return render_template('survey/index.html', informed_consent=Survey.informed_consent)

@survey.route('/1')
def page_one():
    """
    Render the page one template on the /page1 route
    """
    return render_template('survey/page1.html')