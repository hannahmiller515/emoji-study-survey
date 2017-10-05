# app/models.py
# -*- coding: utf-8 -*-

from flask import url_for
from . import engine

get_platforms = '''SELECT platform_id,platform_display_name
                       FROM platforms;'''

get_platform_versions_in_use = '''SELECT platform_id,platform_version_id,version_display_name
                                  FROM platform_versions
                                  WHERE in_use=TRUE
                                  ORDER BY platform_id,release_date desc;'''

# Using emoji_id=935, Woman Dancing emoji, excluding Twitter (version<34) emoji because won't show up
get_emoji_for_device_indicator = '''SELECT renderings.platform_version_id,post_version_id,is_changed,display_url
                                    FROM renderings
                                    JOIN platform_versions ON renderings.platform_version_id=platform_versions.platform_version_id
                                    WHERE emoji_id=935 AND renderings.platform_version_id<34
                                    AND (post_version_id IS NULL OR is_changed=True)
                                    ORDER BY rendering_id;'''

class Survey:

    conn = engine.connect()
    platforms_result = conn.execute(get_platforms)
    platforms_versions = {}
    for platform_id,platform_name in platforms_result.fetchall():
        platforms_versions[platform_id] = {'name':platform_name,'versions':[]}

    platform_versions_result = conn.execute(get_platform_versions_in_use)
    for platform_id,platform_version_id,version_display_name in platform_versions_result.fetchall():
        platforms_versions[platform_id]['versions'].append((platform_version_id,version_display_name))

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
    page_one_age["wrong_handle_error"] = """That doesn't match our records, please try again.
                                            (Hint: make sure you are using your Twitter handle,
                                            which begins with "@", e.g., @UMNEmojiStudy)"""
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
                                the survey, please select the emoji you see here: 💃"""
    device_emoji_result = conn.execute(get_emoji_for_device_indicator)
    conn.close()
    page_two_device["emoji_options"] = []
    skip = False
    for platform_version_id,post_version_id,is_changed,display_url in device_emoji_result.fetchall():
        if skip:
            skip = False
            continue

        img_str = "<img src=\"{0}\" width=\"20px\" />".format(display_url)
        page_two_device["emoji_options"].append((str(platform_version_id),img_str))

        if not post_version_id and not is_changed:
            skip = True
    page_two_device["emoji_options"].append(("0","<img src=\"/static/img/not_supported.png\" />"))
    page_two_device["emoji_options"].append(("-1","I do not see the emoji above as an option."))

    page_two_device["device"] = """Also to help us ensure the survey appears correctly, please
                                indicate which device you are currently using:"""
    page_two_device["device_options"] = [("iPhone","iPhone"),
                                         ("iPad","iPad"),
                                         ("MacBook","MacBook"),
                                         ("iMac","iMac"),
                                         ("Samsung_Phone","Samsung Phone"),
                                         ("Samsung_Tablet","Samsung Tablet"),
                                         ("Google_Phone","Google Phone (e.g., Nexus, Pixel)"),
                                         ("Google_Tablet","Google Tablet (e.g., Nexus, Pixel)"),
                                         ("LG_Phone","LG Phone"),
                                         ("Motorola_Phone","Motorola Phone"),
                                         ("HTC_Phone","HTC Phone"),
                                         ("Amazon_Kindle","Amazon Kindle Fire"),
                                         ("Blackberry_Phone","Blackberry Phone"),
                                         ("Blackberry_Tablet","Blackberry Tablet"),
                                         ("Windows_Phone","Windows Phone"),
                                         ("Windows/Microsoft_Tablet","Windows/Microsoft Tablet"),
                                         ("Windows_LapDesktop","Windows Lap/Desktop"),
                                         ("Linux_LapDesktop","Linux Lap/Desktop"),
                                         ("Other","Other:")]
    page_two_device["device_options_other"] = ["Other"]

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
    page_six_explain["explain0"] = "Since you said you did not know, here is a little explanation:"
    page_six_explain["explain1"] = """To your device, an emoji is just like any other character
                                (e.g., lower-case ‘a’, upper-case ‘B’) and needs to be rendered
                                with a font (e.g., Calibri, Times New Roman). However, for emoji,
                                fonts are unique to device and communication platform vendors.
                                For example, Apple has its own emoji font for iOS/macOS devices
                                (e.g., iPhone, iPad, MacBook), Samsung has its own emoji font for
                                Samsung devices (e.g., Galaxy phones, tablets), etc. Twitter has its
                                own emoji font for when Twitter is viewed in a browser, but users see
                                their own device's emoji when they view Twitter via a device's mobile
                                Twitter app."""
    page_six_explain["explain2"] = """All of this means that a given emoji character looks different
                                      on different device platforms:"""
    page_six_explain["explain3"] = """So when you use an emoji, you see your device’s rendition of
                                the emoji. But when your followers view that emoji, they will see
                                their device’s rendition of the emoji. If your devices have the same
                                emoji font, then you will both see the same rendition of the emoji.
                                But if your devices have different emoji fonts, then you will both
                                see different renditions of the emoji."""
    page_six_explain["describe_reaction"] = "How would you describe your reaction to finding out that this is how emoji function? (Optional)"
    page_six_explain["reaction"] = "If you had to summarize your reaction in one or two words, what would it be?"

    # PAGE SIXE AWARE
    page_six_aware = {}
    page_six_aware["explain0"] = """You say you are aware that emoji are rendered by fonts unique to
                                    device and communication platform vendors. For example, you know
                                    that when you use an emoji on Twitter, it will appear differently
                                    to those who view it depending on which devices it is viewed on."""
    page_six_aware["path"] = """Which of the following best describes how you became aware of this?"""
    page_six_aware["path_options"] = [("1","Personal observation"),
                                      ("2","Someone else told you"),
                                      ("3","You read about it (e.g., in an article)"),
                                      ("4","Other:"),
                                      ("5","Actually, I did not know about this.")]

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
    page_seven_eval["send_tweet"] = """If you had known that this is how your tweet would look to your
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
    page_eight_follow["impression"] = """Now that you are aware that device platforms translate emoji renderings when you
                                        communicate across platforms, please describe your general impression of this:"""
    page_eight_follow["effect_Twitter"] = "In general, do you think this may have any effect on your Twitter communication?"
    page_eight_follow["effect_communication"] = """This is also the way emoji function in communication across platforms
                                                outside of Twitter, like in text messaging for example. Considering
                                                this, do you think this may have any affect on your direct communication
                                                outside of Twitter (e.g., when you directly text a friend)?"""
    page_eight_follow["emoji_applications"] = "Please indicate which of the following applications you use:"
    page_eight_follow["twitter_emoji_frequency"] = "How often do you include emoji in your tweets?"
    page_eight_follow["twitter_emoji_frequency_options"] = [("-2","Almost never"),
                                                            ("-1","Once in a while"),
                                                            ("0","Half of the time"),
                                                            ("1","Pretty often"),
                                                            ("2","Almost every tweet")]
    page_eight_follow["emoji_frequency"] = "In general, how often do you include emoji in your digital communications?"
    page_eight_follow["emoji_frequency_options"] = [("-2","Almost never"),
                                                    ("-1","Once in a while"),
                                                    ("0","Half of the time"),
                                                    ("1","Pretty often"),
                                                    ("2","Most of the time")]

    # PAGE NINE AUDIENCE
    page_nine_audience = {}
    page_nine_audience["audience_description"] = """When you tweet, who do you feel like you're typically targeting?
                                                How would you describe your Twitter following (i.e., those that follow
                                                you on Twitter)?"""
    page_nine_audience["audience"] = "Does your Twitter following contain… (please check all that apply)"
    page_nine_audience["all_devices"] = "Please indicate all devices that you use on a regular basis:"


    # PAGE TEN FUTURE
    page_ten_future = {}
    page_ten_future["future"] = """We may continue this research and we would like to know: Are you open to
                                   us contacting you again for future participation?"""
    page_ten_future["future_options"] = [("yes","Yes, you may contact me again in the future."),
                                         ("no","No, please do not contact me again.")]
    page_ten_future["feedback"] = """Is there anything you'd like to share with us before submitting your survey?
                                     Any comments, feedback, suggestions? (optional)"""

    end_text = "Your survey has been submitted. Thank you so much for your time and participation. Happy tweeting!"

class Queries:
    # RETRIEVAL QUERIES
    handle_query = '''SELECT participant_twitter_handle
                      FROM surveys
                      WHERE survey_id=%s;'''

    tweet_query = '''SELECT tweets.tweet_id,text,source_id
                     FROM tweets
                     JOIN surveys ON surveys.tweet_id=tweets.tweet_id
                     WHERE survey_id=%s;'''

    tweet_fragments_query = '''SELECT is_text,text,emoji_id
                               FROM tweet_fragments
                               WHERE tweet_id=%s
                               ORDER BY sequence_index;'''

    codepoints_query = '''SELECT codepoint_string
                          FROM emoji
                          WHERE emoji_id=%s;'''

    emoji_rendering_img_query = '''SELECT display_url
                                   FROM renderings
                                   WHERE emoji_id=%s AND platform_version_id=%s;'''

    codepoint_rendering_img_query = '''SELECT display_url
                                       FROM renderings
                                       JOIN emoji ON renderings.emoji_id=emoji.emoji_id
                                       WHERE emoji.codepoint_string=%s AND platform_version_id=%s;'''

    platforms_renderings_for_emoji = '''SELECT renderings.platform_version_id,version_name,version_display_name,in_use,is_changed,display_url
                                        FROM renderings
                                        JOIN platform_versions ON renderings.platform_version_id=platform_versions.platform_version_id
                                        WHERE emoji_id=%s AND platform_versions.platform_id=%s
                                        ORDER BY release_date desc;'''

    tweet_analytics = '''UPDATE tweets
                         SET num_tweet_versions=%s,
                             num_unsupported=%s,
                             num_showing_components=%s,
                             num_showing_unsupported=%s,
                             num_showing_component_unsupported_combo=%s
                         WHERE tweet_id=%s'''

    # INSERT QUERIES
    insert_consent_response = '''REPLACE INTO consent_responses(consent,survey_id) VALUES(%s,%s);'''

    insert_wrong_handle_response = '''INSERT INTO wrong_handle_responses(attempt,survey_id) VALUES(%s,%s);'''

    insert_age_response = '''REPLACE INTO age_responses(age,survey_id) VALUES(%s,%s);'''

    insert_device_response = '''REPLACE INTO device_responses(
                                    platform_version_of_emoji,
                                    emoji_not_supported,
                                    emoji_seen_not_option,
                                    device,
                                    device_other,
                                    survey_id) VALUES(%s,%s,%s,%s,%s,%s);'''

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

    insert_aware_response = '''REPLACE INTO aware_responses(
                                            aware_path,
                                            aware_path_other,
                                            aware_explanation,
                                            survey_id) VALUES(%s,%s,%s,%s);'''

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
                                        twitter_emoji_frequency,
                                        emoji_frequency,
                                        impression,
                                        effect_Twitter,
                                        effect_Twitter_explanation,
                                        effect_communication,
                                        effect_communication_explanation,
                                        survey_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'''

    insert_emoji_applications_response = '''REPLACE INTO emoji_applications_responses(
                                            use_Texts,
                                            use_Hangouts,
                                            use_Gmail,
                                            use_Email,
                                            use_Facebook,
                                            use_Messenger,
                                            use_Instagram,
                                            use_Snapchat,
                                            use_Slack,
                                            use_Whatsapp,
                                            survey_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

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
                                            use_on_Other,
                                            Other_desc,
                                            survey_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                              %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                                              %s);'''

    insert_future_contact_response = '''REPLACE INTO future_contact_responses(
                                                future_contact,
                                                survey_id) VALUES(%s,%s);'''

    insert_feedback_response = '''REPLACE INTO feedback_responses(
                                      feedback,
                                      survey_id) VALUES (%s,%s);'''

    survey_started = '''UPDATE surveys
                        SET started=%s
                        WHERE survey_id=%s;'''

    survey_completed = '''UPDATE surveys
                          SET submitted=%s
                          WHERE survey_id=%s;'''

    def get_tweet_for_survey(survey_id):
        conn = engine.connect()
        result = conn.execute(Queries.tweet_query,(survey_id))
        tweet_id,tweet,source_id = result.fetchone()
        result.close()

        # Render the tweet as text so participants see the native emoji, except
        # if the tweet is from the Twitter Web Client, hard code the emoji as Twitter's rendering
        if source_id == 4:
            tweet = ''
            result = conn.execute(Queries.tweet_fragments_query,(tweet_id))
            for is_text,text,emoji_id in result.fetchall():
                if is_text:
                    tweet += text
                else:
                    # 34 is the platform_version_id for the only Twitter platform version (Twemoji 2.3)
                    result = conn.execute(Queries.emoji_rendering_img_query,(emoji_id,34))
                    display_url = result.fetchone()
                    tweet += "<img src=\"{0}\" width=\"20px\" />".format(display_url[0])
                    result.close()

        conn.close()
        return (tweet_id,tweet,source_id)


    def OLD_get_tweet_versions(tweet_id):
        conn = engine.connect()
        tweet_fragments = []
        emoji_platform_versions = {}
        unsupported_count = 0
        platform_version_dict = {}
        emoji_platform_version_renderings = {}
        result = conn.execute(Queries.tweet_fragments_query,(tweet_id))
        for is_text,text,emoji_id in result.fetchall():
            tweet_fragments.append((is_text,text,emoji_id))

            # for an emoji, get all of its eligible renderings
            if not is_text:
                # for each platform, get the renderings of the emoji
                for platform_name,platform_id in Survey.platforms:
                    emoji_platform_versions[platform_id] = []
                    result = conn.execute(Queries.platforms_renderings_for_emoji,(emoji_id,platform_id))
                    skip = False
                    platform_support = False
                    for platform_version_id,version_name,post_version_id,isChanged,display_url in result.fetchall():
                        platform_support = True
                        platform_version_dict[platform_version_id] = (platform_name,version_name)
                        if skip:
                            skip = False
                            continue

                        emoji_platform_version_renderings[(platform_version_id,emoji_id)] = display_url
                        if platform_version_id not in emoji_platform_versions[platform_id]:
                            emoji_platform_versions[platform_id].append(platform_version_id)
                            emoji_platform_versions[platform_id].sort()
                        if not post_version_id and not isChanged:
                            skip = True

                    # If the platform doesn't have a rendering for the emoji character,
                    # increment the negative count of unsupported emoji
                    # add a placeholder in the emoji platform versions list
                    # and a lookup for the platform name that will display in the survey (<Platform name> Device)
                    if not platform_support:
                        unsupported_count-=1
                        emoji_platform_versions[platform_id].append(unsupported_count)
                        platform_version_dict[unsupported_count] = (platform_name,'')


        # TODO show older where doesn't support, not just where change...
        tweets = []
        for platform_name,platform_id in Survey.platforms:
            for platform_version_id in emoji_platform_versions[platform_id]:
                tweet = ''
                for is_text,text,emoji_id in tweet_fragments:
                    if is_text:
                        tweet += text
                    else:
                        display_url = None
                        if platform_version_id > 0:
                            display_url = emoji_platform_version_renderings.get((platform_version_id,emoji_id),None)
                            if not display_url:
                                result = conn.execute(Queries.emoji_rendering_img_query,(emoji_id,platform_version_id))
                                display_url_result = result.fetchone()
                                if display_url_result:
                                    display_url = display_url_result[0]
                                else:
                                    unsupported_count-=1
                                    platform_version_dict[unsupported_count] = (platform_name,'')

                        # Handle if the platform (version) doesn't support the given
                        if not display_url:
                            # TODO handle if platform doesn't support
                            # TODO flag tag sequences?
                            print("{0} doesn't support emoji {1}".format(platform_name,emoji_id))
                            codepoint_string_result = conn.execute(Queries.codepoints_query,(emoji_id))
                            codepoint_string = codepoint_string_result.fetchone()
                            codepoints = codepoint_string[0].split('U+')
                            for codepoint in codepoints[1:]:
                                # Skip U+200D ZWJ, U+FE0F Emoji Presentation Character
                                if codepoint=='200D' or codepoint=='FE0F':
                                    continue

                                result = conn.execute(Queries.codepoint_rendering_img_query,('U+'+codepoint,platform_version_id))
                                display_url_result = result.fetchone()
                                if display_url_result:
                                    tweet += "<img src=\"{0}\" width=\"20px\" />".format(display_url_result[0])
                                else:
                                    tweet += "<img src=\"{0}\" />".format(url_for('static',filename='img/not_supported.png'))
                        else:
                            tweet += "<img src=\"{0}\" width=\"20px\" />".format(display_url)

                (platform_name,version_name) = platform_version_dict[platform_version_id]
                tweets.append((platform_name,version_name,tweet))

        num_tweet_versions = len(tweets)

        # For microsoft and samsung platform versions, remove excess version name info as long as it's not needed to differentiate
        keep_next_long = False
        for i in range(0,num_tweet_versions):
            (platform_name,version_name,tweet) = tweets[i]
            if i<num_tweet_versions-1 and (platform_name=='Microsoft' or platform_name=='Samsung'):
                next_platform_name,next_version_name,next_tweet = tweets[i+1]
                version_name_split = version_name.split(' ')
                short_version_name = ' '.join(version_name_split[:2])
                print('short version of {0}: {1}'.format(version_name,short_version_name))
                if not next_version_name.startswith(short_version_name):
                    if not keep_next_long:
                        tweets[i] = (platform_name,short_version_name,tweet)
                    else:
                        keep_next_long = False
                else:
                    keep_next_long = True

        # TODO store num tweet versions?
        # TODO store num unsupported?
        # TODO what want to store about what was shown?

        return tweets


    def get_tweet_versions(tweet_id):
        conn = engine.connect()
        tweet_fragments = []
        platform_versions_to_render = {}
        platform_version_dict = {}
        emoji_platform_version_renderings = {}
        result = conn.execute(Queries.tweet_fragments_query,(tweet_id))
        for is_text,text,emoji_id in result.fetchall():
            tweet_fragments.append((is_text,text,emoji_id))

            # for an emoji, get all of its eligible renderings
            if not is_text:
                # for each platform, get the renderings of the emoji
                for platform_id,platform_info in Survey.platforms_versions.items():
                    platforms_versions_to_render = []
                    result = conn.execute(Queries.platforms_renderings_for_emoji,(emoji_id,platform_id))

                    # Assume the rendering has changed to include the most recent version,
                    # then working our way back, only include renderings that have changed
                    change_in_between_used_versions = True
                    previous_rendering_version_in_survey = None
                    for platform_version_id,version_name,version_display_name,in_use,is_changed,display_url in result.fetchall():
                        # if it's in use and hasn't changed, update the previous version's device description to include the current version description
                        # only if the current version description isn't already in the list
                        if in_use and not change_in_between_used_versions and platform_version_id not in platform_version_dict:
                            platform_name,prev_display_name = platform_version_dict[previous_rendering_version_in_survey]
                            platform_version_dict[previous_rendering_version_in_survey] = (platform_name,'{0}, {1}'.format(prev_display_name,' '.join(version_display_name.split(' ')[1:])))

                        # show versions that are in use and that have changed, or that haven't changed but will be rendered due to another emoji
                        if in_use and (change_in_between_used_versions or platform_version_id in platform_version_dict):
                            emoji_platform_version_renderings[(platform_version_id,emoji_id)] = display_url
                            platform_version_dict[platform_version_id] = (platform_info['name'],version_display_name)
                            previous_rendering_version_in_survey = platform_version_id
                            change_in_between_used_versions = is_changed
                            if platform_version_id not in platforms_versions_to_render:
                                platforms_versions_to_render.append(platform_version_id)

                        # indicate if the rendering has changed
                        if is_changed:
                            change_in_between_used_versions = True

                    # If the platform doesn't have a rendering for the emoji character,
                    # increment the count of unsupported emoji
                    # add the versions in use to the list to render
                    # (below, will use these versions to either render component codepoints or not supported symbol)
                    if len(platforms_versions_to_render) == 0:
                        """
                        for platform_version_id,platform_version_display_name in platform_info['versions']:
                            platforms_versions_to_render.append(platform_version_id)
                            platform_version_dict[platform_version_id] = (platform_info['name'],platform_version_display_name)
                        """
                        # Instead of the full list (^), default to the most recent version to render an "unsupported" version of the tweet
                        # This approach prevents showing "unsupported" versions of *all* "in use" platform versions
                        # But ignores if past in-use versions have different "unsupported" versions than the most current version (not sure how to easily implement at this point)
                        platform_version_id,platform_version_display_name = platform_info['versions'][0]
                        platforms_versions_to_render.append(platform_version_id)
                        platform_version_dict[platform_version_id] = (platform_info['name'],platform_version_display_name)
                    else:
                        platforms_versions_to_render.sort()

                    platform_versions_to_render[platform_id] = platforms_versions_to_render

        tweets = []
        unsupported_count = 0 # = showing_component_count + showing_unsupported_count + showing_component_unsupported_combo
        showing_components_count = 0
        showing_unsupported_count = 0
        showing_component_unsupported_combo_count = 0
        for platform_id,platform_info in Survey.platforms_versions.items():
            platforms_versions_to_render = platform_versions_to_render[platform_id]
            for platform_version_id in platforms_versions_to_render:
                (platform_name,version_name) = platform_version_dict[platform_version_id]

                tweet = ''
                for is_text,text,emoji_id in tweet_fragments:
                    if is_text:
                        tweet += text
                    else:
                        # Get the rendering for the platform version if we already found it
                        display_url = emoji_platform_version_renderings.get((platform_version_id,emoji_id),None)

                        # If we didn't already find it, check to see if the platform version has a rendering
                        if not display_url:
                            result = conn.execute(Queries.emoji_rendering_img_query,(emoji_id,platform_version_id))
                            display_url_result = result.fetchone()
                            if display_url_result:
                                display_url = display_url_result[0]

                        if display_url:
                            tweet += "<img src=\"{0}\" width=\"20px\" />".format(display_url)

                        # Handle if the platform (version) doesn't support the given emoji:
                        # Render the component codepoints, except for U+200D (the Zero Width Joiner character) and U+FE0F (Emoji Presentation Character)
                        # If the component codepoints aren't supported, render the unsupported character (empty vertical rectangle)
                        else:
                            # TODO handle if platform doesn't support
                            print("{0} {1} doesn't support emoji {2}".format(platform_name,version_name,emoji_id))
                            unsupported_count += 1
                            showing_components = False
                            showing_unsupported = False
                            skip_next = False

                            codepoint_string_result = conn.execute(Queries.codepoints_query,(emoji_id))
                            codepoint_string = codepoint_string_result.fetchone()[0].replace('U+FE0F','')
                            sub_codepoint_strings = codepoint_string.split('U+200D')
                            for sub_codepoint_string in sub_codepoint_strings:
                                result = conn.execute(Queries.codepoint_rendering_img_query,(sub_codepoint_string,platform_version_id))
                                display_url_result = result.fetchone()
                                result.close()
                                if display_url_result:
                                    tweet += "<img src=\"{0}\" width=\"20px\" />".format(display_url_result[0])
                                    showing_components = True
                                else:
                                    codepoints = sub_codepoint_string.split('U+')
                                    for codepoint in codepoints[1:]:
                                        if skip_next:
                                            skip_next = False
                                            continue

                                        result = conn.execute(Queries.codepoint_rendering_img_query,('U+'+codepoint,platform_version_id))
                                        display_url_result = result.fetchone()
                                        result.close()
                                        if display_url_result:
                                            tweet += "<img src=\"{0}\" width=\"20px\" />".format(display_url_result[0])
                                            showing_components = True

                                        if not display_url_result or codepoint=='1F3F4':
                                            # if the codepoint is part of a "REGIONAL INDICATOR" pair (flag)
                                            if codepoint.startswith('1F1E') or codepoint.startswith('1F1F'):
                                                skip_next = True # handle for the pair, then skip the next codepoint
                                                # Get the rendering for the base flag emoji (or unsupported) and the unsupported rendering
                                                result = conn.execute(Queries.codepoint_rendering_img_query,('U+1F3F4',platform_version_id))
                                                display_url_result = result.fetchone()
                                                result.close()
                                                if display_url_result:
                                                    tweet += "<img src=\"{0}\" width=\"20px\" />".format(display_url_result[0])
                                                    showing_components = True
                                                else:
                                                    tweet += "<img src=\"{0}\" />".format(url_for('static',filename='img/not_supported.png'))

                                            tweet += "<img src=\"{0}\" />".format(url_for('static',filename='img/not_supported.png'))
                                            showing_unsupported = True

                                            if codepoint=='1F3F4':
                                                break

                            if showing_components and showing_unsupported:
                                showing_component_unsupported_combo_count += 1
                            else:
                                if showing_components: showing_components_count+=1
                                if showing_unsupported: showing_unsupported_count+=1

                # if only
                version_name = 'Devices' if len(platforms_versions_to_render) == 1 and platform_name != "Twitter" else version_name
                tweets.append((platform_name,version_name,tweet))

        num_tweet_versions = len(tweets)
        conn.execute(Queries.tweet_analytics,(num_tweet_versions,
                                              unsupported_count,
                                              showing_components_count,
                                              showing_unsupported_count,
                                              showing_component_unsupported_combo_count,
                                              tweet_id))
        conn.close()

        return tweets