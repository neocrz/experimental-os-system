from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

DB_URI = os.environ.get('DB_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
DB_EXT = os.environ.get("DB_EXT")

if DB_EXT == "TRUE":
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
else:
    # LOCAL DB
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config["SECRET_KEY"] = SECRET_KEY

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message = "Você precisa logar primeiro!"
login_manager.login_message_category = "info"
from uti import routes