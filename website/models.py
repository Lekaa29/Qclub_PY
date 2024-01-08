from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    
class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    date = db.Column(db.Date)
    res_price = db.Column(db.Integer)
    bottle = db.Column(db.Integer)
    tables = db.relationship('Table')
   
class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taken = db.Column(db.Boolean)
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    
