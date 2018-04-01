from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from restful_ssh_config import BaseModel

APPLICATION = Flask(__name__)
APPLICATION.config.from_pyfile('flask-and-descendants.cfg')
DATABASE = SQLAlchemy(APPLICATION, model_class=BaseModel)
MARSHMALLOW = Marshmallow(APPLICATION)
