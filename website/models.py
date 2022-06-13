from __future__ import annotations

from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salary = db.Column(db.Float)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    finances = db.relationship('Finance')
