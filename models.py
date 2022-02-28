from numpy import unique
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100))
    points = db.Column(db.Integer)