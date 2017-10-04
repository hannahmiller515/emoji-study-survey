# app/survey/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import InputRequired,Length

from ..models import Survey

class ConsentForm(FlaskForm):
    consent = RadioField(choices=Survey.informed_consent["options"],
                         validators=[InputRequired("Please provide your statement of consent.")])
    submit = SubmitField('>>')

class AgeForm(FlaskForm):
    handle = StringField("Twitter Handle", validators=[InputRequired("Please enter your twitter handle."),
                                                       Length(max=15,message="Please enter a valid twitter handle, 15 characters or less.")])
    age = RadioField(choices=Survey.page_one_age["age_options"],
                     validators=[InputRequired("Please select your age.")])
    submit = SubmitField('>>')

class DeviceForm(FlaskForm):
    emoji = RadioField(choices=Survey.page_two_device["emoji_options"],
                       validators=[InputRequired("Required")])
    device = RadioField(choices=Survey.page_two_device["device_options"],
                        validators=[InputRequired("Required")])
    Other = StringField()
    submit = SubmitField('>>')

class AppearForm(FlaskForm):
    appear = RadioField(choices=Survey.yes_no_options,
                        validators=[InputRequired("Required")])
    appear_explanation = TextAreaField(Survey.explain)
    submit = SubmitField('>>')

class EmojiRoleForm(FlaskForm):
    needs_emoji = RadioField(choices=Survey.page_four_emojirole["likert_options"],
                             validators=[InputRequired("Required")])
    could_remove = RadioField(choices=Survey.page_four_emojirole["likert_options"],
                              validators=[InputRequired("Required")])
    could_substitute = RadioField(choices=Survey.page_four_emojirole["likert_options"],
                                  validators=[InputRequired("Required")])
    submit = SubmitField('>>')

class ExposeForm(FlaskForm):
    aware = RadioField(choices=Survey.page_five_expose["expose_options"],
                       validators=[InputRequired("Required")])
    submit = SubmitField('>>')

class ExplainForm(FlaskForm):
    describe_reaction = TextAreaField(Survey.page_six_explain["describe_reaction"])
    reaction = StringField(Survey.page_six_explain["reaction"],validators=[InputRequired("Required")])
    submit = SubmitField('>>')

class AwareForm(FlaskForm):
    path = RadioField(choices=Survey.page_six_aware["path_options"],
                      validators=[InputRequired("Required")])
    path_other = StringField()
    path_explanation = TextAreaField(Survey.explain)
    submit = SubmitField('>>')

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
    submit = SubmitField('>>')

class FollowForm(FlaskForm):
    impression = TextAreaField(Survey.page_eight_follow["impression"])
    effect_Twitter = RadioField(choices=Survey.yes_no_options,
                                validators=[InputRequired("Required")])
    effect_Twitter_explanation = TextAreaField(Survey.explain)

    twitter_emoji_frequency = RadioField(choices=Survey.page_eight_follow["twitter_emoji_frequency_options"],
                                 validators=[InputRequired("Required")])

    effect_communication = RadioField(choices=Survey.yes_no_options,
                                      validators=[InputRequired("Required")])
    effect_communication_explanation = TextAreaField(Survey.explain)

    # applications checkboxes
    use_Texts = BooleanField("Text Messages")
    use_Hangouts = BooleanField("Google Hangouts")
    use_Gmail = BooleanField("Gmail")
    use_Email = BooleanField("Email (not Gmail)")
    use_Facebook = BooleanField("Facebook")
    use_Messenger = BooleanField("Facebook Messenger")
    use_Instagram = BooleanField("Instagram")
    use_Snapchat = BooleanField("Snapchat")
    use_Slack = BooleanField("Slack")
    use_Whatsapp = BooleanField("WhatsApp")

    emoji_frequency = RadioField(choices=Survey.page_eight_follow["emoji_frequency_options"],
                                 validators=[InputRequired("Required")])

    submit = SubmitField('>>')

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
    use_on_Samsung_Phone = BooleanField("Samsung Phone")
    use_on_Samsung_Tablet = BooleanField("Samsung Tablet")
    use_on_Google_Phone = BooleanField("Google Phone (e.g., Nexus, Pixel)")
    use_on_Google_Tablet = BooleanField("Google Tablet (e.g., Nexus, Pixel)")
    use_on_LG_Phone = BooleanField("LG Phone")
    use_on_Motorola_Phone = BooleanField("Motorola Phone")
    use_on_HTC_Phone = BooleanField("HTC Phone")
    use_on_Amazon_Kindle = BooleanField("Amazon Kindle Fire")
    use_on_Blackberry_Phone = BooleanField("Blackberry Phone")
    use_on_Blackberry_Tablet = BooleanField("Blackberry Tablet")
    use_on_Windows_Phone = BooleanField("Windows Phone")
    use_on_Windows_Tablet = BooleanField("Windows/Microsoft Tablet")
    use_on_Windows_LapDesktop = BooleanField("Windows Lap/Desktop")
    use_on_Linux_LapDesktop = BooleanField("Linux Lap/Desktop")
    use_on_Other = BooleanField("Other:")
    Other_desc = StringField()

    submit = SubmitField('>>')

class FutureForm(FlaskForm):
    contact_in_future = RadioField(choices=Survey.page_ten_future["future_options"],
                                   validators=[InputRequired("Required")])
    submit = SubmitField('>>')