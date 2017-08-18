# app/survey/views.py

from flask import render_template

from . import survey

@survey.route('/')
def landing_page():
    """
    Render the informed consent template on the / route
    TODO capture url id!
    """
    return render_template('survey/index.html', title="UMN Emoji Study")

@survey.route('/foo')
def landing_page():
    """
    Render the informed consent template on the / route
    TODO capture url id!
    """
    return render_template('survey/index.html', title="UMN Emoji Study")

@survey.route('/page1')
def page_one():
    """
    Render the page one template on the /page1 route
    """
    return render_template('survey/page1.html', title="UMN Emoji Study")