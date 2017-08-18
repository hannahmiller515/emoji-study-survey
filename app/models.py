# app/models.py

from app import db

class Participant(db.Model):
    """
    Create a Participant table
    """
           
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