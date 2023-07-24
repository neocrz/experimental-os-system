from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config["SECRET_KEY"] = "92797c0346bdf993c1de5eee"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from uti import routes