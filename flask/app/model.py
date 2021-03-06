from . import db
from datetime import datetime

class Users(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=False, unique=True, nullable=False)
    password = db.Column(db.String(255), index=False, unique=False, nullable=False)
    phone = db.Column(db.String(20), index=False, unique=True, nullable=False)
    email = db.Column(db.String(255), index=False, unique=True, nullable=False)
    create_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

class Products(db.Model):

    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=False, unique=True, nullable=False)
    stars = db.Column(db.Integer, index=False, unique=False, nullable=False)
    price = db.Column(db.Integer, index=False, unique=False, nullable=False)
    create_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)
