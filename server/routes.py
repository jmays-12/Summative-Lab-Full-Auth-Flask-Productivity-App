#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource

from config import app, db, api
from models import User, Movie


@app.before_request
def check_logged_in():
    open_access_list = ['Signup', 'Login', 'CheckSession']

    if request.endpoint not in open_access_list and 'user_id' not in session:
        return {'error': '401 Unauthorized'}, 401


class Signup(Resource):
    def post(self):
        data = request.get_json() or {}

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'error': 'username and password are required'}, 422

        user = User(username=username)
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        return user.to_dict(), 201


class Login(Resource):
    def post(self):
        data = request.get_json() or {}

        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'error': 'invalid username or password'}, 401


class Logout(Resource):
    def delete(self):
        session['user_id'] = None

        return {}, 204


class CheckSession(Resource):
    def get(self):
        user = User.query.filter_by(id=session.get('user_id')).first()

        if user:
            return user.to_dict(), 200

        return {'error': 'not logged in'}, 401

class Movies(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        movies = Movie.query.filter_by(
            user_id=session['user_id']
        ).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return {
            'movies': [movie.to_dict() for movie in movies.items],
            'total': movies.total,
            'page': movies.page,
            'pages': movies.pages
        }, 200

    def post(self):
        data = request.get_json() or {}

        title = data.get('title')
        genre = data.get('genre')
        rating = data.get('rating')
        watched_on = data.get('watched_on')

        if not title or not genre:
            return {'error': 'title and genre are required'}, 422

        movie = Movie(
            title=title,
            genre=genre,
            rating=rating,
            watched_on=watched_on,
            user_id=session['user_id']
        )

        db.session.add(movie)
        db.session.commit()

        return movie.to_dict(), 201

class MovieByID(Resource):
    def patch(self, id):
        movie = Movie.query.filter_by(
            id=id,
            user_id=session['user_id']
        ).first()

        if not movie:
            return {'error': 'movie not found'}, 404

        data = request.get_json() or {}

        if 'title' in data:
            movie.title = data['title']
        if 'genre' in data:
            movie.genre = data['genre']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'watched_on' in data:
            movie.watched_on = data['watched_on']

        db.session.commit()

        return movie.to_dict(), 200

    def delete(self, id):
        movie = Movie.query.filter_by(
            id=id,
            user_id=session['user_id']
        ).first()

        if not movie:
            return {'error': 'movie not found'}, 404

        db.session.delete(movie)
        db.session.commit()

        return {}, 204


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Movies, '/movies')
api.add_resource(MovieByID, '/movies/<int:id>')
