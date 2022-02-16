from src import db
from src.routes import index

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    displayname = db.Column(db.String(64))
    email = db.Column(db.String(128), index=True, unique=True)
    pwd = db.Column(db.String(128))
    
    def __repr__(self):
        return f'User {self.displayname}'