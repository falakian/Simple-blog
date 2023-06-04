from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask (__name__)
app.config['SECRET_KEY'] = '04edbb5c1ca8ba4b6351d416c412c974'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../blog.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = ' Please login first '
login_manager.login_message_category = 'info'
from blog import routes