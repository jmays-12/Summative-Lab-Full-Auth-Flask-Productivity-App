#!/usr/bin/env python3
# Standard Library
import os

# Third-party
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv

# walks up to find .env file so it works from /server or project root
load_dotenv()

app = Flask(__name__)
# secret key signs the session cookie to keep login state between requests
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
CORS(app)
api = Api(app)