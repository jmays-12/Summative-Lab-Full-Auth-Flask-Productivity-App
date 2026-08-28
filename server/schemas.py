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
        validate=validate.Length(min=1, error='title cannot be blank'),
    )
    genre = fields.Str(required=False, allow_none=True)
    rating = fields.Int(
        required=False,
        allow_none=True,
        validate=validate.Range(min=0, max=10, error='rating must be 0-10'),
    )
    watched_on = fields.Str(required=False, allow_none=True)


user_schema = UserSchema()
movie_schema = MovieSchema()
# partial=True lets PATCH send only the fields it's actually changing
movie_schema_partial = MovieSchema(partial=True)