# app/survey/views.py

from flask import render_template, redirect, send_from_directory, url_for, request
import os

from . import survey
from .forms import ConsentForm,AgeForm,DeviceForm,AppearForm,EmojiRoleForm,ExposeForm,ExplainForm,EvalForm,FollowForm,AudienceForm,FutureForm
from ..models import Survey

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
    # POST
    if request.method == "POST" and form.validate_on_submit():
        if form.consent.data == "no":
            return redirect(url_for('survey.consent_not_given'))
        elif form.consent.data == "yes":
            return redirect(url_for('survey.page_one_age'))

    # GET
    # Get the survey id out of the URL
    if survey_id != None:
        Survey.survey_id = survey_id
    else:
        return redirect("http://z.umn.edu/emojistudy")
    return render_template('survey/informed_consent.html', form=form, informed_consent=Survey.informed_consent)

@survey.route('/survey/consent_not_given')
def consent_not_given():
    return render_template('survey/no_consent.html', no_consent=Survey.informed_consent["no_consent"])

@survey.route('/survey/1', methods=['GET','POST'])
def page_one_age():
    form = AgeForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        if form.age.data == "0":
            return redirect(url_for("survey.under_18"))

        Survey.handle = form.handle.data
        Survey.age = int(form.age.data)

        return redirect(url_for('survey.page_two_device'))

    #GET
    return render_template('survey/page1-age.html', form=form, form_text=Survey.page_one_age)

@survey.route('/survey/under18')
def under_18():
    return render_template('survey/under18.html', under_18=Survey.page_one_age["under_18"])

@survey.route('/survey/2', methods=['GET','POST'])
def page_two_device():
    form = DeviceForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        emoji = form.emoji.data
        device = form.device.data
        device_other = None
        if device == "iOS_Other":
            device_other = form.iOS_Other.data
        elif device == "Samsung_Other":
            device_other = form.Samsung_Other.data
        elif device == "Google_Other":
            device_other = form.Google_Other.data
        elif device == "LG_Other":
            device_other = form.LG_Other.data
        elif device == "Motorola_Other":
            device_other = form.Motorola_Other.data
        elif device == "HTC_Other":
            device_other = form.HTC_Other.data
        elif device == "Blackberry_Other":
            device_other = form.Blackberry_Other.data
        elif device == "Windows_Other":
            device_other = form.Windows_Other.data
        elif device == "Other":
            device_other = form.Other.data

        Survey.emoji_device_indicator = emoji
        Survey.device = device
        Survey.device_other = device_other

        return redirect(url_for('survey.page_three_appear'))

    #GET
    return render_template('survey/page2-device.html', form=form, form_text=Survey.page_two_device)

@survey.route('/survey/3', methods=['GET','POST'])
def page_three_appear():
    form = AppearForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        Survey.appear = form.appear.data
        if not form.appear_explanation.data == '':
            Survey.appear_explanation = form.appear_explanation.data
        return redirect(url_for('survey.page_four_emojirole'))

    #GET
    return render_template('survey/page3-appear.html', form=form, form_text=Survey.page_three_appear)

@survey.route('/survey/4', methods=['GET','POST'])
def page_four_emojirole():
    form = EmojiRoleForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        Survey.needs_emoji = form.needs_emoji.data
        Survey.could_remove = form.could_remove.data
        Survey.could_substitute = form.could_substitute.data
        return redirect(url_for('survey.page_five_expose'))

    #GET
    return render_template('survey/page4-emojirole.html', form=form, form_text=Survey.page_four_emojirole)

@survey.route('/survey/5', methods=['GET','POST'])
def page_five_expose():
    form = ExposeForm()

    # POST
    if request.method == "POST" and form.validate_on_submit():
        if form.aware.data == "no":
            Survey.aware = False
            return redirect(url_for('survey.page_six_explain'))
        elif form.aware.data == "yes":
            Survey.aware = True
            #TODO figure out what to do for those that already know
            #return redirect(url_for('survey.'))

    # GET
    return render_template('survey/page5-expose.html', form=form, form_text=Survey.page_five_expose)

@survey.route('/survey/6', methods=['GET','POST'])
def page_six_explain():
    form = ExplainForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        Survey.reaction = form.reaction.data
        if not form.describe_reaction.data == '':
            Survey.describe_reaction = form.describe_reaction.data
        return redirect(url_for('survey.page_seven_eval'))

    #GET
    return render_template('survey/page6-explain.html', form=form, form_text=Survey.page_six_explain)

@survey.route('/survey/7', methods=['GET','POST'])
def page_seven_eval():
    form = EvalForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        Survey.same_message = form.same_message.data
        if not form.same_message_explanation == '':
            Survey.same_message_explanation = form.same_message_explanation.data
        Survey.same_interpretation = form.same_interpretation.data
        if not form.same_interpretation_explanation == '':
            Survey.same_interpretation_explanation = form.same_interpretation_explanation.data
        Survey.send_tweet = form.send_tweet.data
        if not form.send_tweet_explanation == '':
            Survey.send_tweet_explanation = form.send_tweet_explanation.data
        Survey.edit_tweet = form.edit_tweet.data
        if not form.edit_tweet_other == '':
            Survey.edit_tweet_other = form.edit_tweet_other.data
    return render_template('survey/page7-eval.html', form=form, form_text=Survey.page_seven_eval)

@survey.route('/survey/8', methods=['GET','POST'])
def page_eight_follow():
    form = FollowForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        Survey.emoji_frequency = form.emoji_frequency.data
        Survey.effect_Twitter = form.effect_Twitter.data
        Survey.effect_communication = form.effect_communication.data
        if not form.impression.data == '':
            Survey.impression = form.impression.data
        if not form.effect_Twitter_explanation.data == '':
            Survey.effect_Twitter_explanation = form.effect_Twitter_explanation.data
        if not form.effect_communication_explanation == '':
            Survey.effect_communication_explanation = form.effect_communication_explanation.data
        return redirect(url_for('survey.page_nine_audience'))

    #GET
    return render_template('survey/page8-follow.html', form=form, form_text=Survey.page_eight_follow)

@survey.route('/survey/9', methods=['GET','POST'])
def page_nine_audience():
    form = AudienceForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        if not form.audience_description.data == '':
            Survey.audience_description = form.audience_description.data

        Survey.friends_in_audience = form.friends_in_audience.data
        Survey.family_in_audience = form.family_in_audience.data
        Survey.professional_in_audience = form.professional_in_audience.data
        Survey.online_only_in_audience = form.online_only_in_audience.data
        Survey.strangers_in_audience = form.strangers_in_audience.data
        Survey.other_in_audience = form.other_in_audience.data
        if not form.other_in_audience_desc.data == '':
            Survey.other_in_audience_desc = form.other_in_audience_desc.data

        Survey.use_on_iPhone = form.use_on_iPhone.data
        Survey.use_on_iPad = form.use_on_iPad.data
        Survey.use_on_MacBook = form.use_on_MacBook.data
        Survey.use_on_iMac = form.use_on_iMac.data
        Survey.use_on_iOS_Other = form.use_on_iOS_Other.data
        if not form.iOS_Other_desc.data == '':
            Survey.iOS_Other_desc = form.iOS_Other_desc.data
        Survey.use_on_Samsung_Phone = form.use_on_Samsung_Phone.data
        Survey.use_on_Samsung_Tablet = form.use_on_Samsung_Tablet.data
        Survey.use_on_Samsung_Other = form.use_on_Samsung_Other.data
        if not form.Samsung_Other_desc.data == '':
            Survey.Samsung_Other_desc = form.Samsung_Other_desc.data
        Survey.use_on_Google_Phone = form.use_on_Google_Phone.data
        Survey.use_on_Google_Tablet = form.use_on_Google_Tablet.data
        Survey.use_on_Google_Other = form.use_on_Google_Other.data
        if not form.Google_Other_desc.data == '':
            Survey.Google_Other_desc = form.Google_Other_desc.data
        Survey.use_on_LG_Phone = form.use_on_LG_Phone.data
        Survey.use_on_LG_Other = form.use_on_LG_Other.data
        if not form.LG_Other_desc.data == '':
            Survey.LG_Other_desc = form.LG_Other_desc.data
        Survey.use_on_Motorola_Phone = form.use_on_Motorola_Phone.data
        Survey.use_on_Motorola_Other = form.use_on_Motorola_Other.data
        if not form.Motorola_Other_desc.data == '':
            Survey.Motorola_Other_desc = form.Motorola_Other_desc.data
        Survey.use_on_HTC_Phone = form.use_on_HTC_Phone.data
        Survey.use_on_HTC_Other = form.use_on_HTC_Other.data
        if not form.HTC_Other_desc.data == '':
            Survey.HTC_Other_desc = form.HTC_Other_desc.data
        Survey.use_on_Amazon_Kindle = form.use_on_Amazon_Kindle.data
        Survey.use_on_Blackberry_Phone = form.use_on_Blackberry_Phone.data
        Survey.use_on_Blackberry_Tablet = form.use_on_Blackberry_Tablet.data
        Survey.use_on_Blackberry_Other = form.use_on_Blackberry_Other.data
        if not form.Blackberry_Other_desc.data == '':
            Survey.Blackberry_Other_desc = form.Blackberry_Other_desc.data
        Survey.use_on_Windows_Phone = form.use_on_Windows_Phone.data
        Survey.use_on_Windows_Tablet = form.use_on_Windows_Tablet.data
        Survey.use_on_Windows_Laptop = form.use_on_Windows_Laptop.data
        Survey.use_on_Windows_Desktop = form.use_on_Windows_Desktop.data
        Survey.use_on_Windows_Other = form.use_on_Windows_Other.data
        if not form.Windows_Other_desc.data == '':
            Survey.Windows_Other_desc = form.Windows_Other_desc.data
        Survey.use_on_Other = form.use_on_Other.data
        if not form.Other_desc.data == '':
            Survey.Other_desc = form.Other_desc.data
        return redirect(url_for('survey.page_ten_future'))

    #GET
    return render_template('survey/page9-audience.html', form=form, form_text=Survey.page_nine_audience)

@survey.route('/survey/10', methods=['GET','POST'])
def page_ten_future():
    form = FutureForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        print(form.contact_in_future.data)
        Survey.contact_in_future = form.contact_in_future.data
        return redirect(url_for('survey.end_survey'))

    return render_template('survey/page10-future.html', form=form, form_text=Survey.page_ten_future)

@survey.route('/survey/end')
def end_survey():
    return render_template('survey/end.html', end_text=Survey.end_text)