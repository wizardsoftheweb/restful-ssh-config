from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

APPLICATION = Flask(__name__)
APPLICATION.config.from_pyfile('flask-and-descendants.cfg')
DATABASE = SQLAlchemy(APPLICATION)
MARSHMALLOW = Marshmallow(APPLICATION)
