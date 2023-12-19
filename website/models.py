from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    
class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taken = db.Column(db.Boolean)
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    