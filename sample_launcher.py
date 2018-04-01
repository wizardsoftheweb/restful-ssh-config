from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('flask-and-descendants.cfg')
db = SQLAlchemy(app)
ma = Marshmallow(app)