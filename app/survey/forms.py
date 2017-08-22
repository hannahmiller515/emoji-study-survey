# app/survey/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField, BooleanField
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

class AudienceForm(FlaskForm):
    audience_description = TextAreaField(Survey.page_nine_audience["audience_description"])

    # following checkboxes
    friends_in_audience = BooleanField("Friends")
    family_in_audience = BooleanField("Family")
    professional_in_audience = BooleanField("Professional Connections")
    online_only_in_audience = BooleanField("Online-only Connections")
    strangers_in_audience = BooleanField("Strangers")
    other_in_audience = BooleanField("Other:")
    other_in_audience_desc = StringField()

    # device checkboxes
    use_on_iPhone = BooleanField("iPhone")
    use_on_iPad = BooleanField("iPad")
    use_on_MacBook = BooleanField("MacBook")
    use_on_iMac = BooleanField("iMac")
    use_on_iOS_Other = BooleanField("iOS Other:")
    iOS_Other_desc = StringField()
    use_on_Samsung_Phone = BooleanField("Samsung Phone")
    use_on_Samsung_Tablet = BooleanField("Samsung Tablet")
    use_on_Samsung_Other = BooleanField("Samsung Other:")
    Samsung_Other_desc = StringField()
    use_on_Google_Phone = BooleanField("Google Phone")
    use_on_Google_Tablet = BooleanField("Google Tablet")
    use_on_Google_Other = BooleanField("Google Other:")
    Google_Other_desc = StringField()
    use_on_LG_Phone = BooleanField("LG Phone")
    use_on_LG_Other = BooleanField("LG Other")
    LG_Other_desc = StringField()
    use_on_Motorola_Phone = BooleanField("Motorola Phone")
    use_on_Motorola_Other = BooleanField("Motorola Other:")
    Motorola_Other_desc = StringField()
    use_on_HTC_Phone = BooleanField("HTC Phone")
    use_on_HTC_Other = BooleanField("HTC Other:")
    HTC_Other_desc = StringField()
    use_on_Amazon_Kindle = BooleanField("Amazon Kindle")
    use_on_Blackberry_Phone = BooleanField("Blackberry Phone")
    use_on_Blackberry_Tablet = BooleanField("Blackberry Tablet")
    use_on_Blackberry_Other = BooleanField("Blackberry Other:")
    Blackberry_Other_desc = StringField()
    use_on_Windows_Phone = BooleanField("Windows Phone")
    use_on_Windows_Tablet = BooleanField("Windows/Microsoft Tablet")
    use_on_Windows_Laptop = BooleanField("Windows Laptop")
    use_on_Windows_Desktop = BooleanField("Windows Desktop")
    use_on_Windows_Other = BooleanField("Windows Other:")
    Windows_Other_desc = StringField()
    use_on_Other = BooleanField("Other:")
    Other_desc = StringField()
    submit = SubmitField('Next >>')

class FutureForm(FlaskForm):
    contact_in_future = RadioField(choices=Survey.page_ten_future["future_options"],
                                   validators=[InputRequired("Required")])
    submit = SubmitField('Submit Survey')