# app/survey/views.py

from flask import render_template, redirect, send_from_directory, url_for, request
import os

from . import survey
from .forms import ConsentForm
from ..models import Survey

@survey.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(survey.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@survey.route('/')
def route_to_website():
    return redirect("http://z.umn.edu/emojistudy")

@survey.route('/survey/id/<survey_id>', methods=['GET','POST'])
def informed_consent(survey_id=None):
    """
    Render the informed consent template on the / route
    TODO capture url id!
    """
    form = ConsentForm()
    print(form.consent.data)
    # POST
    if request.method == "POST" and form.validate_on_submit():
        if form.consent.data == "no":
            return redirect(url_for('survey.consent_not_given'))
        elif form.consent.data == "yes":
            return redirect(url_for('survey.page_one'))

    # GET
    # Get the survey id out of the URL
    if survey_id != None:
        Survey.survey_id = survey_id
    else:
        return redirect("http://z.umn.edu/emojistudy")
    return render_template('survey/index.html', form=form, informed_consent=Survey.informed_consent)

@survey.route('/survey/1')
def page_one():
    """
    Render the page one template on the /page1 route
    """
    return render_template('survey/page1.html', survey_id=Survey.survey_id)

@survey.route('/survey/consent_not_given')
def consent_not_given():
    return render_template('survey/no_consent.html', no_consent=Survey.informed_consent["no_consent"])