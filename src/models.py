from src import db
from src import login

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    displayname = db.Column(db.String(64))
    email = db.Column(db.String(128), index=True, unique=True)
    pwd = db.Column(db.String(128))

    posts = db.relationship('Post', backref='author', lazy = 'dynamic')
    
    def __repr__(self):
        return f'User {self.displayname}'

    def set_password(self, password):
        self.pwd = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwd, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    body = db.Column(db.String(2048))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'[{self.title}]: [{self.body}]'
