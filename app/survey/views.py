# app/survey/views.py

import datetime
from flask import render_template, redirect, url_for, request, session

from . import survey
from .forms import ConsentForm,AgeForm,DeviceForm,AppearForm,EmojiRoleForm,ExposeForm,ExplainForm,AwareForm,EvalForm,FollowForm,AudienceForm,FutureForm
from ..models import Survey,Queries
from .. import engine

@survey.route('/')
def route_to_website():
    return redirect("http://z.umn.edu/emojistudy")

@survey.route('/survey/id/<survey_id>', methods=['GET','POST'])
def informed_consent(survey_id=None):
    """
    Render the informed consent template on the / route
    """
    form = ConsentForm()
    conn = engine.connect()

    # POST
    if request.method == "POST" and form.validate_on_submit():
        if form.consent.data == "no":
            conn.execute(Queries.insert_consent_response, (False, session['survey_id']))
            conn.close()
            return redirect(url_for('survey.consent_not_given'))
        elif form.consent.data == "yes":
            conn.execute(Queries.insert_consent_response, (True, session['survey_id']))
            conn.close()
            return redirect(url_for('survey.page_one_age'))

    # GET
    # Get the survey id out of the URL and make sure it's a valid survey id
    if survey_id != None:
        survey_id_int = int(survey_id)
        result = conn.execute(Queries.handle_query,(survey_id_int))
        survey_handle_result = result.fetchone()
        if survey_handle_result:
            session['twitter_handle'] = survey_handle_result[0].lower()
        else:
            return redirect("http://z.umn.edu/emojistudy")

        conn.execute(Queries.survey_started,(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),survey_id_int))
        conn.close()
        session['survey_id'] = survey_id_int

    else:
        return redirect("http://z.umn.edu/emojistudy")
    return render_template('survey/informed_consent.html', form=form, informed_consent=Survey.informed_consent)

@survey.route('/survey/consent_not_given')
def consent_not_given():
    return render_template('survey/no_consent.html', no_consent=Survey.informed_consent["no_consent"])

@survey.route('/survey/1', methods=['GET','POST'])
def page_one_age():
    form = AgeForm()
    handle_error = '';

    #POST
    if request.method == "POST" and form.validate_on_submit():
        conn = engine.connect()
        handle = form.handle.data.lower()
        survey_handle = session['twitter_handle']
        if survey_handle != handle and ('@' + survey_handle) != handle:
            conn.execute(Queries.insert_wrong_handle_response,(handle,session['survey_id']))
            conn.close()
            handle_error = Survey.page_one_age["wrong_handle_error"]
            return render_template('survey/page1-age.html', form=form, form_text=Survey.page_one_age, handle_error=handle_error)

        age = int(form.age.data)
        conn.execute(Queries.insert_age_response, (age, session['survey_id']))
        conn.close()

        if age == 0:
            return redirect(url_for("survey.under_18"))

        return redirect(url_for('survey.page_two_device'))

    #GET
    return render_template('survey/page1-age.html', form=form, form_text=Survey.page_one_age, handle_error=handle_error)

@survey.route('/survey/handle_error')
def wrong_handle():
    return render_template('survey/wrong_handle.html', wrong_handle=Survey.page_one_age["wrong_handle"])

@survey.route('/survey/under18')
def under_18():
    return render_template('survey/under18.html', under_18=Survey.page_one_age["under_18"])

@survey.route('/survey/2', methods=['GET','POST'])
def page_two_device():
    form = DeviceForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        emoji_device_indicator = int(form.emoji.data)
        emoji_not_supported = False
        emoji_seen_not_option = False
        if emoji_device_indicator == 0:
            emoji_not_supported = True
            emoji_device_indicator = None
        elif emoji_device_indicator == -1:
            emoji_seen_not_option = True
            emoji_device_indicator = None

        device = form.device.data
        device_other = None
        if device == "Other":
            device_other = form.Other.data

        conn = engine.connect()
        conn.execute(Queries.insert_device_response, (emoji_device_indicator,
                                                      emoji_not_supported,
                                                      emoji_seen_not_option,
                                                      device,
                                                      device_other,
                                                      session['survey_id']))
        conn.close()

        return redirect(url_for('survey.page_three_appear'))

    #GET
    return render_template('survey/page2-device.html', form=form, form_text=Survey.page_two_device)

@survey.route('/survey/3', methods=['GET','POST'])
def page_three_appear():
    form = AppearForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        appear = None
        appear_explanation = None
        if form.appear.data == 'no':
            appear = False
        elif form.appear.data == 'yes':
            appear = True
        if not form.appear_explanation.data == '':
            appear_explanation = form.appear_explanation.data

        conn = engine.connect()
        conn.execute(Queries.insert_appearance_response, (appear, appear_explanation, session['survey_id']))
        conn.close()

        return redirect(url_for('survey.page_four_emojirole'))

    #GET
    tweet_id,tweet,source_id = Queries.get_tweet_for_survey(session['survey_id'])
    session['tweet_id'] = tweet_id
    session['tweet'] = tweet
    return render_template('survey/page3-appear.html', form=form, form_text=Survey.page_three_appear, tweet=tweet)

@survey.route('/survey/4', methods=['GET','POST'])
def page_four_emojirole():
    form = EmojiRoleForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        needs_emoji = int(form.needs_emoji.data)
        could_remove = int(form.could_remove.data)
        could_substitute = int(form.could_substitute.data)

        conn = engine.connect()
        conn.execute(Queries.insert_emoji_role_response, (needs_emoji, could_remove, could_substitute, session['survey_id']))
        conn.close()

        return redirect(url_for('survey.page_five_expose'))

    #GET
    tweet = session.get('tweet',None)
    if not tweet:
        tweet_id,tweet,source_id = Queries.get_tweet_for_survey(session['survey_id'])
        session['tweet_id'] = tweet_id
        session['tweet'] = tweet
    return render_template('survey/page4-emojirole.html', form=form, form_text=Survey.page_four_emojirole, tweet=tweet)

@survey.route('/survey/5', methods=['GET','POST'])
def page_five_expose():
    form = ExposeForm()

    # POST
    if request.method == "POST" and form.validate_on_submit():
        conn = engine.connect()
        if form.aware.data == "no":
            aware = False
            conn.execute(Queries.insert_awareness_response, (aware, session['survey_id']))
            conn.close()
            return redirect(url_for('survey.page_six_explain'))

        elif form.aware.data == "yes":
            aware = True
            conn.execute(Queries.insert_awareness_response, (aware, session['survey_id']))
            conn.close()
            return redirect(url_for('survey.page_six_aware'))

    # GET
    tweet = session.get('tweet',None)
    if not tweet:
        tweet_id,tweet,source_id = Queries.get_tweet_for_survey(session['survey_id'])
        session['tweet_id'] = tweet_id
        session['tweet'] = tweet
    tweets = Queries.get_tweet_versions(session['tweet_id'])
    session['tweets'] = tweets
    return render_template('survey/page5-expose.html', form=form, form_text=Survey.page_five_expose,tweet=tweet,tweets=tweets)

@survey.route('/survey/6-explain', methods=['GET','POST'])
def page_six_explain():
    form = ExplainForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        reaction = form.reaction.data
        describe_reaction = None
        if not form.describe_reaction.data == '':
            describe_reaction = form.describe_reaction.data

        conn = engine.connect()
        conn.execute(Queries.insert_reaction_response, (describe_reaction, reaction, session['survey_id']))
        conn.close()

        return redirect(url_for('survey.page_seven_eval'))

    #GET
    return render_template('survey/page6-explain.html', form=form, form_text=Survey.page_six_explain)

@survey.route('/survey/6-aware', methods=['GET','POST'])
def page_six_aware():
    form = AwareForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        aware_path = int(form.path.data)

        aware_path_other = None
        if not form.path_other.data == '':
            aware_path_other = form.path_other.data
        aware_explanation = None
        if not form.path_explanation.data == '':
            aware_explanation = form.path_explanation.data

        conn = engine.connect()
        conn.execute(Queries.insert_aware_response, (aware_path, aware_path_other, aware_explanation, session['survey_id']))
        conn.close()

        if aware_path == 5:
            return redirect(url_for("survey.page_six_explain"))

        return redirect(url_for('survey.page_seven_eval'))

    #GET
    return render_template('survey/page6-aware.html', form=form, form_text=Survey.page_six_aware)

@survey.route('/survey/7', methods=['GET','POST'])
def page_seven_eval():
    form = EvalForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        same_message = form.same_message.data
        same_message_explanation = None
        if not form.same_message_explanation == '':
            same_message_explanation = form.same_message_explanation.data

        same_interpretation = form.same_interpretation.data
        same_interpretation_explanation = None
        if not form.same_interpretation_explanation == '':
            same_interpretation_explanation = form.same_interpretation_explanation.data

        send_tweet = None
        send_tweet_explanation = None
        if form.send_tweet.data == 'no':
            send_tweet = False
        elif form.send_tweet.data == 'yes':
            send_tweet = True
        if not form.send_tweet_explanation == '':
            send_tweet_explanation = form.send_tweet_explanation.data

        edit_tweet = int(form.edit_tweet.data)
        edit_tweet_other = None
        if not form.edit_tweet_other == '':
            edit_tweet_other = form.edit_tweet_other.data

        conn = engine.connect()
        conn.execute(Queries.insert_evaluation_response, (same_message, same_message_explanation,
                                                          same_interpretation, same_interpretation_explanation,
                                                          send_tweet, send_tweet_explanation,
                                                          edit_tweet, edit_tweet_other, session['survey_id']))
        conn.close()

        return redirect(url_for('survey.page_eight_follow'))

    #GET
    tweet = session.get('tweet',None)
    if not tweet:
        tweet_id,tweet,source_id = Queries.get_tweet_for_survey(session['survey_id'])
        session['tweet_id'] = tweet_id
        session['tweet'] = tweet

    tweets = session.get('tweets',None)
    if not tweets:
        tweets = Queries.get_tweet_versions(session['tweet_id'])
        session['tweets'] = tweets
    return render_template('survey/page7-eval.html', form=form, form_text=Survey.page_seven_eval, tweet=tweet, tweets=tweets)

@survey.route('/survey/8', methods=['GET','POST'])
def page_eight_follow():
    form = FollowForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        twitter_emoji_frequency = int(form.twitter_emoji_frequency.data)
        emoji_frequency = int(form.emoji_frequency.data)

        impression = None
        if not form.impression.data == '':
            impression = form.impression.data

        effect_Twitter = None
        effect_Twitter_explanation = None
        if form.effect_Twitter.data == 'no':
            effect_Twitter = False
        elif form.effect_Twitter.data == 'yes':
            effect_Twitter = True
        if not form.effect_Twitter_explanation.data == '':
            effect_Twitter_explanation = form.effect_Twitter_explanation.data

        effect_communication = None
        effect_communication_explanation = None
        if form.effect_communication.data == 'no':
            effect_communication = False
        elif form.effect_communication.data == 'yes':
            effect_communication = True
        if not form.effect_communication_explanation.data == '':
            effect_communication_explanation = form.effect_communication_explanation.data

        conn = engine.connect()
        conn.execute(Queries.insert_follow_response, (twitter_emoji_frequency, emoji_frequency,
                                                      impression, effect_Twitter, effect_Twitter_explanation,
                                                      effect_communication, effect_communication_explanation,
                                                      session['survey_id']))

        use_Texts = form.use_Texts.data
        use_Hangouts = form.use_Hangouts.data
        use_Gmail = form.use_Gmail.data
        use_Email = form.use_Email.data
        use_Facebook = form.use_Facebook.data
        use_Messenger = form.use_Messenger.data
        use_Instagram = form.use_Instagram.data
        use_Snapchat = form.use_Snapchat.data
        use_Slack = form.use_Slack.data
        use_Whatsapp = form.use_Whatsapp.data

        conn.execute(Queries.insert_emoji_applications_response, (use_Texts,
                                                                  use_Hangouts,
                                                                  use_Gmail,
                                                                  use_Email,
                                                                  use_Facebook,
                                                                  use_Messenger,
                                                                  use_Instagram,
                                                                  use_Snapchat,
                                                                  use_Slack,
                                                                  use_Whatsapp,
                                                                  session['survey_id']))
        conn.close()

        return redirect(url_for('survey.page_nine_audience'))

    #GET
    return render_template('survey/page8-follow.html', form=form, form_text=Survey.page_eight_follow)

@survey.route('/survey/9', methods=['GET','POST'])
def page_nine_audience():
    form = AudienceForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        # AUDIENCE DATA
        audience_description = None
        if not form.audience_description.data == '':
            audience_description = form.audience_description.data

        friends_in_audience = form.friends_in_audience.data
        family_in_audience = form.family_in_audience.data
        professional_in_audience = form.professional_in_audience.data
        online_only_in_audience = form.online_only_in_audience.data
        strangers_in_audience = form.strangers_in_audience.data
        other_in_audience = form.other_in_audience.data
        other_in_audience_desc = None
        if not form.other_in_audience_desc.data == '':
            other_in_audience_desc = form.other_in_audience_desc.data

        conn = engine.connect()
        conn.execute(Queries.insert_audience_response, (audience_description, friends_in_audience,
                                                                              family_in_audience,
                                                                              professional_in_audience,
                                                                              online_only_in_audience,
                                                                              strangers_in_audience,
                                                                              other_in_audience, other_in_audience_desc, session['survey_id']))
        # ALL DEVICES DATA
        use_on_iPhone = form.use_on_iPhone.data
        use_on_iPad = form.use_on_iPad.data
        use_on_MacBook = form.use_on_MacBook.data
        use_on_iMac = form.use_on_iMac.data

        use_on_Samsung_Phone = form.use_on_Samsung_Phone.data
        use_on_Samsung_Tablet = form.use_on_Samsung_Tablet.data

        use_on_Google_Phone = form.use_on_Google_Phone.data
        use_on_Google_Tablet = form.use_on_Google_Tablet.data

        use_on_LG_Phone = form.use_on_LG_Phone.data

        use_on_Motorola_Phone = form.use_on_Motorola_Phone.data

        use_on_HTC_Phone = form.use_on_HTC_Phone.data

        use_on_Amazon_Kindle = form.use_on_Amazon_Kindle.data

        use_on_Blackberry_Phone = form.use_on_Blackberry_Phone.data
        use_on_Blackberry_Tablet = form.use_on_Blackberry_Tablet.data

        use_on_Windows_Phone = form.use_on_Windows_Phone.data
        use_on_Windows_Tablet = form.use_on_Windows_Tablet.data
        use_on_Windows_LapDesktop = form.use_on_Windows_LapDesktop.data

        use_on_Linux_LapDesktop = form.use_on_Linux_LapDesktop.data

        use_on_Other = form.use_on_Other.data
        Other_desc = None
        if not form.Other_desc.data == '':
            Other_desc = form.Other_desc.data

        conn.execute(Queries.insert_all_devices_response, (use_on_iPhone,
                                                           use_on_iPad,
                                                           use_on_MacBook,
                                                           use_on_iMac,
                                                           use_on_Samsung_Phone,
                                                           use_on_Samsung_Tablet,
                                                           use_on_Google_Phone,
                                                           use_on_Google_Tablet,
                                                           use_on_LG_Phone,
                                                           use_on_Motorola_Phone,
                                                           use_on_HTC_Phone,
                                                           use_on_Amazon_Kindle,
                                                           use_on_Blackberry_Phone,
                                                           use_on_Blackberry_Tablet,
                                                           use_on_Windows_Phone,
                                                           use_on_Windows_Tablet,
                                                           use_on_Windows_LapDesktop,
                                                           use_on_Linux_LapDesktop,
                                                           use_on_Other, Other_desc,
                                                           session['survey_id']))
        conn.close()
        return redirect(url_for('survey.page_ten_future'))

    #GET
    return render_template('survey/page9-audience.html', form=form, form_text=Survey.page_nine_audience)

@survey.route('/survey/10', methods=['GET','POST'])
def page_ten_future():
    form = FutureForm()

    #POST
    if request.method == "POST" and form.validate_on_submit():
        if form.contact_in_future.data == 'no':
            contact_in_future = False
        if form.contact_in_future.data == 'yes':
            contact_in_future = True

        conn = engine.connect()
        conn.execute(Queries.insert_future_contact_response, (contact_in_future, session['survey_id']))

        feedback = None
        if not form.feedback.data == '':
            feedback = form.feedback.data

        conn.execute(Queries.insert_feedback_response,(feedback, session['survey_id']))
        conn.close()

        return redirect(url_for('survey.end_survey'))

    return render_template('survey/page10-future.html', form=form, form_text=Survey.page_ten_future)

@survey.route('/survey/end')
def end_survey():
    conn = engine.connect()
    conn.execute(Queries.survey_completed,(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),session['survey_id']))
    conn.close()

    session.pop('survey_id', None)
    session.pop('twitter_handle', None)
    session.pop('tweet_id',None)
    session.pop('tweet',None)
    session.pop('tweets',None)

    return render_template('survey/end.html', end_text=Survey.end_text)