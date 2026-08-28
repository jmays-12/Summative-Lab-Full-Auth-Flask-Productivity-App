#!/usr/bin/env python3
from sqlalchemy.orm import validates

from config import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    movies = db.relationship('Movie', backref='user')

    @property
    def password_hash(self):
        raise AttributeError('Password hash cannot be viewed')

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        ).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

    @validates('username')
    def validate_username(self, key, username):
        if not username or not username.strip():
            raise ValueError('Username cannot be blank')
        return username

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
        }


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    rating = db.Column(db.Integer)
    watched_on = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @validates('title')
    def validate_title(self, key, title):
        if not title or not title.strip():
            raise ValueError('title cannot be blank')
        if len(title) > 50:
            raise ValueError('title must be 50 characters or fewer')
        return title

    @validates('genre')
    def validate_genre(self, key, genre):
        if genre and len(genre) > 30:
            raise ValueError('genre must be 30 characters or fewer')
        return genre

    @validates('rating')
    def validate_rating(self, key, rating):
        if rating < 0 or rating > 10:
            raise ValueError('rating must be 0-10')
        return rating

    @validates('watched_on')
    def validate_watched_on(self, key, watched_on):
        if watched_on and len(watched_on) > 20:
            raise ValueError('watched on must be 20 characters or fewer')
        return watched_on

    

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'rating': self.rating,
            'watched_on': self.watched_on,
            'user_id': self.user_id,
        }