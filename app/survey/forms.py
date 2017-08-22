# app/survey/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import InputRequired,DataRequired

from ..models import Survey

class ConsentForm(FlaskForm):
    consent = RadioField(choices=Survey.informed_consent["options"],
                         validators=[InputRequired("Please provide your statement of consent.")])
    submit = SubmitField('Submit')

class AgeForm(FlaskForm):
    handle = StringField("Twitter Handle", validators=[InputRequired("Please enter your twitter handle.")])
    age = RadioField(choices=Survey.page_one_age["age_options"],
                     validators=[InputRequired("Please select your age.")])
    submit = SubmitField('Next >>')

class DeviceForm(FlaskForm):
    emoji = RadioField(choices=Survey.page_two_device["emoji_options"],
                       validators=[InputRequired("Required")])
    device = RadioField(choices=Survey.page_two_device["device_options"],
                        validators=[InputRequired("Required")])
    iOS_Other = StringField()
    Samsung_Other = StringField()
    Google_Other = StringField()
    LG_Other = StringField()
    Motorola_Other = StringField()
    HTC_Other = StringField()
    Blackberry_Other = StringField()
    Windows_Other = StringField()
    Other = StringField()
    submit = SubmitField('Next >>')

class AppearForm(FlaskForm):
    appear = RadioField(choices=Survey.yes_no_options,
                        validators=[InputRequired("Required")])
    appear_explanation = TextAreaField(Survey.explain)
    submit = SubmitField('Next >>')

class EmojiRoleForm(FlaskForm):
    needs_emoji = RadioField(choices=Survey.page_four_emojirole["likert_options"],
                             validators=[InputRequired("Required")])
    could_remove = RadioField(choices=Survey.page_four_emojirole["likert_options"],
                              validators=[InputRequired("Required")])
    could_substitute = RadioField(choices=Survey.page_four_emojirole["likert_options"],
                                  validators=[InputRequired("Required")])
    submit = SubmitField('Next >>')

class ExposeForm(FlaskForm):
    aware = RadioField(choices=Survey.page_five_expose["expose_options"],
                       validators=[InputRequired("Required")])
    submit = SubmitField('Next >>')

class ExplainForm(FlaskForm):
    describe_reaction = TextAreaField(Survey.page_six_explain["describe_reaction"])
    reaction = StringField(Survey.page_six_explain["reaction"],validators=[InputRequired("Required")])
    submit = SubmitField('Next >>')

class EvalForm(FlaskForm):
    same_message = RadioField(choices=Survey.page_seven_eval["same_message_options"],
                              validators=[InputRequired("Required")])
    same_message_explanation = TextAreaField(Survey.explain)
    same_interpretation = RadioField(choices=Survey.page_seven_eval["same_interpretation_options"],
                                     validators=[InputRequired("Required")])
    same_interpretation_explanation = TextAreaField(Survey.explain)
    send_tweet = RadioField(choices=Survey.yes_no_options,
                            validators=[InputRequired("Required")])
    send_tweet_explanation = TextAreaField(Survey.explain)
    edit_tweet = RadioField(choices=Survey.page_seven_eval["edit_tweet_options"],
                            validators=[InputRequired("Required")])
    edit_tweet_other = StringField()
    submit = SubmitField('Next >>')

class FollowForm(FlaskForm):
    emoji_frequency = RadioField(choices=Survey.page_eight_follow["emoji_frequency_options"],
                                 validators=[InputRequired("Required")])
    impression = TextAreaField(Survey.page_eight_follow["impression"])
    effect_Twitter = RadioField(choices=Survey.yes_no_options,
                                validators=[InputRequired("Required")])
    effect_Twitter_explanation = TextAreaField(Survey.explain)
    effect_communication = RadioField(choices=Survey.yes_no_options,
                                      validators=[InputRequired("Required")])
    effect_communication_explanation = TextAreaField(Survey.explain)
    submit = SubmitField('Next >>')