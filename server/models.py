#!/usr/bin/env python3
from config import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)

    movies = db.relationship('Movie', backref='user')


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    rating = db.Column(db.Integer)
    watched_on = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))