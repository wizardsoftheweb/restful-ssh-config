"""
This file provides a sample app launcher.

This content is essentially the same thing as ``application.py``. It will most
likely be removed in the future.
"""
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config.from_pyfile('restful_ssh_config/flask-and-descendants.cfg')
DB = SQLAlchemy(APP)
MA = Marshmallow(APP)
