# app/models.py
# -*- coding: utf-8 -*-

class Survey:

    # COMMON
    show_tweet = "You recently tweeted:"
    explain = "Please explain your answer (optional):"
    yes_no_options = [("yes","Yes"),("no","No")]

    # INFORMED CONSENT
    informed_consent = {}
    informed_consent["intro"] = """Thank you for participating! But first, we ask that you read
                                the following information and ask any questions you may have
                                before agreeing to complete this survey."""
    informed_consent["purpose_header"] = "Purpose and Procedure:"
    informed_consent["purpose"] = """We are studying how people understand and interact with emoji,
                                and we invite you to take part in this survey (~5 minutes required)
                                to help us further our research by providing some feedback about one
                                of your recent emoji interactions on Twitter, as well as about your
                                understanding of emoji in general. The goal of this survey is to learn 
                                whether the way emoji function affects people so that we may better 
                                understand the role they play in communication."""
    informed_consent["contact_header"] = "Contacts and Questions:"
    informed_consent["contact"] = """This survey is being conducted by researchers in the Computer Science 
                                and Engineering Department at the University of Minnesota. If you have 
                                any questions about this study, please feel free to contact the researchers 
                                at emojistudy@umn.edu. If you have any questions or concerns regarding 
                                this study and would like to talk to someone other than the researchers, 
                                you are encouraged to contact the Research Subjects' Advocate Line,
                                D528 Mayo, 420 Delaware St. Southeast, Minneapolis, MN 55455; (612) 625-1650."""
    informed_consent["voluntary_header"] = "Participation is Voluntary:"
    informed_consent["voluntary"] = """Participation in this study is voluntary. You may exit from the 
                                survey at any time, and your decision whether or not to participate will 
                                not affect your current or future relations with the University of Minnesota."""
    informed_consent["statement_header"] = "Statement of Consent:"
    informed_consent["statement"] = "After reading the above passage, please select whether you consent to participate:"
    informed_consent["options"] = [("yes","I agree to participate"),
                                   ("no","I do not agree to participate")]
    informed_consent["no_consent"] = "We understand. Thank you for your time!"

    # PAGE ONE HANDLE / AGE
    page_one_age = {}
    page_one_age["handle"] = """This survey is tailored specifically to you and your twitter activity.
                                Please enter your Twitter handle to help us confirm that we have the correct data:"""
    page_one_age["wrong_handle"] = """We're sorry, but we do not have the correct data for the Twitter handle you
                                      entered. Thank you for your time!"""
    page_one_age["age"] = "Please select your age:"
    page_one_age["age_options"] = [("0","< 18"),
                                   ("1","18-25"),
                                   ("2","26-35"),
                                   ("3","36-45"),
                                   ("4","46-55"),
                                   ("5","56+")]
    page_one_age["under_18"] = """We appreciate your willingness to help us out, but unfortunately we can only include
                                people that are at least 18 years old. Thank you for your time!"""

    # PAGE TWO DEVICE
    page_two_device = {}
    page_two_device["emoji"] = """To help us ensure that emoji are appearing correctly in
                                the survey, please select the emoji you see here: 😉"""
    # TODO emoji options
    page_two_device["emoji_options"] = [("version1","<img src=\"https://emojipedia-us.s3.amazonaws.com/thumbs/120/apple/96/winking-face_1f609.png\" width=\"20px\" />")]
    page_two_device["device"] = """Also to help us ensure the survey appears correctly, please
                                indicate which device you are currently using:"""
    page_two_device["device_options"] = [("iPhone","iPhone"),
                                         ("iPad","iPad"),
                                         ("MacBook","MacBook"),
                                         ("iMac","iMac"),
                                         ("iOS_Other","iOS Other:"),
                                         ("Samsung_Phone","Samsung Phone"),
                                         ("Samsung_Tablet","Samsung Tablet"),
                                         ("Samsung_Other","Samsung Other:"),
                                         ("Google_Phone","Google Phone"),
                                         ("Google_Tablet","Google Tablet"),
                                         ("Google_Other","Google Other:"),
                                         ("LG_Phone","LG Phone"),
                                         ("LG_Other","LG Other:"),
                                         ("Motorola_Phone","Motorola Phone"),
                                         ("Motorola_Other","Motorola Other:"),
                                         ("HTC_Phone","HTC Phone"),
                                         ("HTC_Other","HTC Other:"),
                                         ("Amazon_Kindle","Amazon Kindle"),
                                         ("Blackberry_Phone","Blackberry Phone"),
                                         ("Blackberry_Tablet","Blackberry Tablet"),
                                         ("Blackberry_Other","Blackberry Other:"),
                                         ("Windows_Phone","Windows Phone"),
                                         ("Windows/Microsoft_Tablet","Windows/Microsoft Tablet"),
                                         ("Windows_Laptop","Windows Laptop"),
                                         ("Windows_Desktop","Windows Desktop"),
                                         ("Windows_Other","Windows Other:"),
                                         ("Other","Other:")]
    page_two_device["device_options_other"] = ["iOS_Other","Samsung_Other","Google_Other","LG_Other",
                                               "Motorola_Other","HTC_Other","Blackberry_Other","Windows_Other",
                                               "Other"]

    # PAGE THREE APPEAR
    page_three_appear = {}
    page_three_appear["show_tweet"] = show_tweet
    page_three_appear["appear"] = "Do you think that this tweet will appear exactly this way to everyone who views it?"

    # PAGE FOUR EMOJI ROLE
    page_four_emojirole = {}
    page_four_emojirole["show_tweet"] = show_tweet
    page_four_emojirole["emoji_role"] = """How important is the emoji to this tweet? Please select
                                    your level of agreement with the following statements:"""
    page_four_emojirole["needs_emoji"] = "This tweet needs this emoji to convey what I meant."
    page_four_emojirole["could_remove"] = "The emoji could be removed from this tweet and it would not make a difference."
    page_four_emojirole["could_substitute"] = "A different emoji could be substituted for this emoji in this tweet and not change my meaning."
    page_four_emojirole["likert_options"] = [("-2","Strongly Disagree"),
                                          ("-1","Disagree"),
                                          ("0","Not Sure"),
                                          ("1","Agree"),
                                          ("2","Strongly Agree")]

    # PAGE FIVE EXPOSE
    page_five_expose = {}
    page_five_expose["show_tweet"] = show_tweet
    page_five_expose["expose"] = """Did you know that the emoji in your tweet will appear differently
                                to other users on Twitter? For example, your tweet will appear
                                as the following on the associated devices / operating systems:"""
    page_five_expose["expose_options"] = [("yes","Yes, I knew this."),
                                          ("no","No, I did not know this.")]

    # PAGE_SIX_EXPLAIN
    page_six_explain = {}
    page_six_explain["here"] = "Since you said you did not know, here is a little explanation:"
    page_six_explain["explain1"] = """To your device, an emoji is just like any other character
                                (e.g., lower-case ‘a’, upper-case ‘B’) and needs to be rendered
                                with a font. However, for emoji, fonts are unique to each device
                                platform. For example, Apple has its own emoji font for iOS devices
                                (e.g., iPhone, iPad, MacBook), Google has its own font for Android
                                and Google devices (e.g., Nexus), etc. This means that the same
                                emoji character looks different on different device platforms:"""
    page_six_explain["explain2"] = """So when you use an emoji, you see your device’s rendition of
                                the emoji. But when your followers view that emoji, they will see
                                their device’s rendition of the emoji. If your devices have the same
                                emoji font, then you will both see the same rendition of the emoji.
                                But if your devices have different emoji fonts, then you will both
                                see different renditions of the emoji."""
    page_six_explain["describe_reaction"] = "How would you describe your reaction to finding out that this is how emoji function? (Optional)"
    page_six_explain["reaction"] = "If you had to summarize your reaction in one or two words, what would it be?"

    # PAGE SEVEN EVAL
    page_seven_eval = {}
    page_seven_eval["show_tweet"] = "Your tweet (what you see):"
    page_seven_eval["followers_see"] = "What your followers see:"
    page_seven_eval["same_message"] = """Do you think your followers’ versions of the tweet convey
                                         the same message you intended to send with your tweet?"""
    page_seven_eval["same_message_options"] = [("yes","<b>Yes</b>, I think my followers' versions convey the same message."),
                                               ("some","I think <b>some</b> of my followers' versions convey the same message, some do not."),
                                               ("no","<b>No</b>, I think my followers' versions do not convey the same message.")]
    page_seven_eval["same_interpretation"] = "Do you think your followers will interpret your tweet the same way you do?"
    page_seven_eval["same_interpretation_options"] = [("yes","<b>Yes</b>, I think my followers will interpret my tweet the same way."),
                                                      ("some","I think <b>some</b> of my followers will interpret my tweet the same way, some will not."),
                                                      ("no","<b>No</b>, I think my followers will not interpret my tweet the same way.")]
    page_seven_eval["send_tweet"] = """If you had you known that this is how your tweet would look to your
                                 audience, would you have sent it as is?"""
    page_seven_eval["edit_tweet"] = "How would you edit your tweet knowing this is how it looks to your audience?"
    page_seven_eval["edit_tweet_options"] = [("0","I would not edit my tweet."),
                                       ("1","I would edit the text in my tweet."),
                                       ("2","I would add another emoji to my tweet."),
                                       ("3","I would replace the emoji with another in my tweet."),
                                       ("4","I would remove the emoji from my tweet."),
                                       ("5","Other:")]

    # PAGE EIGHT FOLLOW
    page_eight_follow = {}
    page_eight_follow["emoji_frequency"] = "How often do you include emoji in your tweets?"
    page_eight_follow["emoji_frequency_options"] = [("0","Never"),
                                                    ("1","Once in a while"),
                                                    ("2","Pretty often"),
                                                    ("3","Almost every tweet")]
    page_eight_follow["impression"] = """Now that you are aware that device platforms translate emoji renderings when you
                                        communicate across platforms, please describe your general impression of this:"""
    page_eight_follow["effect_Twitter"] = "In general, do you think this may have any effect on your Twitter communication?"
    page_eight_follow["effect_communication"] = """This is also the way emoji function in communication across platforms
                                                outside of Twitter, like in SMS text messaging for example. Considering
                                                this, do you think this may have any affect on your direct communication
                                                outside of Twitter (e.g., when you directly text a friend)?"""

    # PAGE NINE AUDIENCE
    page_nine_audience = {}
    page_nine_audience["audience_description"] = """When you tweet, who do you feel like you're typically targeting?
                                                How would you describe your Twitter following (i.e., those that follow
                                                you on Twitter)?"""
    page_nine_audience["audience"] = "Does your Twitter following contain… (please check all that apply)"
    page_nine_audience["all_devices"] = "Please indicate all devices that you use Twitter on:"

    # PAGE TEN FUTURE
    page_ten_future = {}
    page_ten_future["future"] = """We may continue this research and we would like to know: Are you open to
                                   us contacting you again for future participation?"""
    page_ten_future["future_options"] = [("yes","Yes, you may contact me again in the future."),
                                         ("no","No, please do not contact me again.")]

    end_text = "Your survey has been submitted. Thank you so much for your time and participation. Happy tweeting!"

class Queries:
    # RETRIEVAL QUERIES
    handle_query = '''SELECT participant_twitter_handle FROM surveys WHERE survey_id=%s;'''

    tweet_query = '''SELECT tweets.tweet_id,text,source_id
                     FROM tweets
                     JOIN surveys ON surveys.tweet_id=tweets.tweet_id
                     WHERE survey_id=%s;'''

    tweet_fragments_query = '''SELECT is_text,text,emoji_id
                               FROM tweet_fragments
                               WHERE tweet_id=%s
                               ORDER BY sequence_index;'''

    emoji_rendering_img_query = '''SELECT display_url FROM renderings WHERE emoji_id=%s AND platform_version_id=%s;'''

    # INSERT QUERIES
    insert_consent_response = '''REPLACE INTO consent_responses(consent,survey_id) VALUES(%s,%s);'''

    insert_age_response = '''REPLACE INTO age_responses(age,survey_id) VALUES(%s,%s);'''

    #TODO handle emoji device indicator
    insert_device_response = '''REPLACE INTO device_responses(
                                    device,
                                    device_other,
                                    survey_id) VALUES(%s,%s,%s);'''

    insert_appearance_response = '''REPLACE INTO appearance_responses(
                                        appears_same,
                                        explanation,
                                        survey_id) VALUES(%s,%s,%s);'''

    insert_emoji_role_response = '''REPLACE INTO emoji_role_responses(
                                        needs_emoji,
                                        could_remove,
                                        could_substitute,
                                        survey_id) VALUES(%s,%s,%s,%s);'''

    insert_awareness_response = '''REPLACE INTO awareness_responses(
                                            is_aware,
                                            survey_id) VALUES(%s,%s);'''

    insert_reaction_response = '''REPLACE INTO reaction_responses(
                                            reaction_explanation,
                                            reaction_short,
                                            survey_id) VALUES(%s,%s,%s);'''

    insert_evaluation_response = '''REPLACE INTO evaluation_responses(
                                            same_message,
                                            same_message_explanation,
                                            same_interpretation,
                                            same_interpretation_explanation,
                                            send_tweet,
                                            send_tweet_explanation,
                                            edit_tweet,
                                            edit_tweet_other,
                                            survey_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

    insert_follow_response = '''REPLACE INTO follow_responses(
                                        emoji_frequency,
                                        impression,
                                        effect_Twitter,
                                        effect_Twitter_explanation,
                                        effect_communication,
                                        effect_communication_explanation,
                                        survey_id) VALUES(%s,%s,%s,%s,%s,%s,%s);'''

    insert_audience_response = '''REPLACE INTO audience_responses(
                                        audience_description,
                                        friends_in_audience,
                                        family_in_audience,
                                        professional_in_audience,
                                        online_only_in_audience,
                                        strangers_in_audience,
                                        other_in_audience,
                                        other_in_audience_desc,
                                        survey_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

    insert_all_devices_response = '''REPLACE INTO all_devices_responses(
                                            use_on_iPhone,
                                            use_on_iPad,
                                            use_on_MacBook,
                                            use_on_iMac,
                                            use_on_iOS_Other,
                                            iOS_Other_desc,
                                            use_on_Samsung_Phone,
                                            use_on_Samsung_Tablet,
                                            use_on_Samsung_Other,
                                            Samsung_Other_desc,
                                            use_on_Google_Phone,
                                            use_on_Google_Tablet,
                                            use_on_Google_Other,
                                            Google_Other_desc,
                                            use_on_LG_Phone,
                                            use_on_LG_Other,
                                            LG_Other_desc,
                                            use_on_Motorola_Phone,
                                            use_on_Motorola_Other,
                                            Motorola_Other_desc,
                                            use_on_HTC_Phone,
                                            use_on_HTC_Other,
                                            HTC_Other_desc,
                                            use_on_Amazon_Kindle,
                                            use_on_Blackberry_Phone,
                                            use_on_Blackberry_Tablet,
                                            use_on_Blackberry_Other,
                                            Blackberry_Other_desc,
                                            use_on_Windows_Phone,
                                            use_on_Windows_Tablet,
                                            use_on_Windows_Laptop,
                                            use_on_Windows_Desktop,
                                            use_on_Windows_Other,
                                            Windows_Other_desc,
                                            use_on_Other,
                                            Other_desc,
                                            survey_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                              %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                              %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                              %s,%s,%s,%s,%s,%s,%s);'''

    insert_future_contact_response = '''REPLACE INTO future_contact_responses(
                                                future_contact,
                                                survey_id) VALUES(%s,%s);'''
