from settings import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    role = db.Column(db.String(24))
    password_hash = db.Column(db.String(128))
    blogObjects = db.relationship('BlogObject', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class BlogObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogType = db.Column(db.String(10))
    title = db.Column(db.String(20))
    image = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(240))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<BlogObject {}>'.format(self.id)