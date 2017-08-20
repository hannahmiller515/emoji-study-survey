# app/models.py

#from app import db

class Survey:
    survey_id = None

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




"""
class Participant(db.Model):
    # Create a Participant table
           
    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key=True)
    twitter_id = db.Column(db.String(60), index=True, unique=True)
    screen_name = db.Column(db.String(20), index=True, unique=True)
    display_name = db.Column(db.String(60), index=True, unique=True)
    #created_at = db.Column(db.)
    friends_count = db.Column(db.Integer)
    followers_count = db.Column(db.Integer)
    statuses_count = db.Column(db.Integer)
    favourites_count = db.Column(db.Integer)
    is_participant = db.Column(db.Boolean, default=False)
    
    #department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    #role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #is_admin = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return '<Participant: {}>'.format(self.screen_name)
"""