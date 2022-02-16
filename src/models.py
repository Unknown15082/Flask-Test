from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    displayname = db.Column(db.String(64))
    email = db.Column(db.String(128), index=True, unique=True)
    pwd = db.Column(db.String(128))

    posts = db.relationship('Post', backref='author', lazy = 'dynamic')
    
    def __repr__(self):
        return f'User {self.displayname}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    body = db.Column(db.String(2048))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'[{self.title}]: [{self.body}]'
