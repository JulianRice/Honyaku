from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
'''
About UserMixin - It Contains:
[1] is_authenticated: a property that is True if the user has valid credentials
[2] is_active: a property that is True if the user's account is active
[3] is_anonymous: a property that is False for regular users
[4] get_id(): a method that returns a unique identifier for the user as a string

Running Instructions for DB
flask db init
flask db upgrade
flask db downgrade
flask shell

Updating a model
1. flask db migrate -m "new fields in user model"
2. flask db upgrade
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
    about_me = db.Column(db.String(200))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def Avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def SetPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def CheckPassword(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)