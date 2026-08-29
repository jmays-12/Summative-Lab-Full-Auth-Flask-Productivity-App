#!/usr/bin/env python3
"""Wipe and reseed the dev database with a couple of users + movies."""
from faker import Faker

from config import app, db
from models import User, Movie

fake = Faker()

with app.app_context():
    print('Clearing db...')
    Movie.query.delete()
    User.query.delete()

    print('Seeding users...')
    users = []
    for username in ['alice', 'bob', 'charlie', 'daniel']:
        user = User(username=username)
        user.password_hash = 'password123'
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    print('Seeding movies...')
    genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror']
    movies = []
    for user in users:
        for _ in range(5):
            movies.append(Movie(
                title=fake.catch_phrase(),
                genre=fake.random_element(elements=genres),
                rating=fake.random_int(min=1, max=10),
                # date_object() not date() - date() gives back a string, we need an actual date to match the model
                watched_on=fake.date_object(),
                user_id=user.id,
            ))
    db.session.add_all(movies)
    db.session.commit()

    print('Done seeding!')
