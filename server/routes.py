#!/usr/bin/env python3
from flask import request, session
from flask_restful import Resource

from config import api, app

@app.before_request
def check_logged_in():
    open_access_list = ['Signup', 'Login', 'CheckSession']

    if request.endpoint not in open_access_list and 'user_id' not in session:
        return {'error': '401 Unauthorized'}, 401
    
class Signup(Resource):
    def post(self):
        pass


class Login(Resource):
    def post(self):
        pass


class Logout(Resource):
    def delete(self):
        pass


class CheckSession(Resource):
    def get(self):
        pass


class Movies(Resource):
    def get(self):
        pass

    def post(self):
        pass


class MovieByID(Resource):
    def patch(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Movies, '/movies')
api.add_resource(MovieByID, '/movies/<int:id>')