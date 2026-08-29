#!/usr/bin/env python3
from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    username = fields.Str(
        required=True,
        validate=validate.Length(min=1, error='username cannot be blank'),
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=6, error='password must be at least 6 characters'),
    )


class MovieSchema(Schema):
    title = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=50, error='title must be 1-50 characters'),
    )
    genre = fields.Str(
        required=False,
        allow_none=True,
        validate=validate.Length(max=30, error='genre must be 30 characters or fewer'),
    )
    rating = fields.Int(
        required=False,
        allow_none=True,
        validate=validate.Range(min=0, max=10, error='rating must be 0-10'),
    )
    watched_on = fields.Date(
        required=False,
        allow_none=True,
        error_messages={'invalid': 'watched_on must be a valid date (YYYY-MM-DD)'},
    )


user_schema = UserSchema()
movie_schema = MovieSchema()
# partial=True so patch can just send one field its changing instead of needing everything
movie_schema_partial = MovieSchema(partial=True)