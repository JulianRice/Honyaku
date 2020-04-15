from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

'''
About UserMixin - It Contains:
[1] is_authenticated: a property that is True if the user has valid credentials
[2] is_active: a property that is True if the user's account is active
[3] is_anonymous: a property that is False for regular users
[4] get_id(): a method that returns a unique identifier for the user as a string
'''

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    eFirst = db.Column(db.String(64), index=True)
    eLast = db.Column(db.String(64), index=True)
    jFirst = db.Column(db.String(64), index=True)
    jLast = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))

    def SetPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def CheckPassword(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)