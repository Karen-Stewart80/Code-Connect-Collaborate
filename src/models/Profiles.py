from main import db

class Profiles(db.Model):
    __tablename__ = 'profiles'

    userid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    userpass = db.Column(db.String(), nullable=False)
    profile_pic = db.Column(db.String())
    account_active = db.Column(db.Boolean(), default = True)
    email = db.Column(db.String(), nullable=False)
    github = db.Column(db.String())
