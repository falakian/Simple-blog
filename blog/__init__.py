from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask (__name__)
app.config['SECRET_KEY'] = '04edbb5c1ca8ba4b6351d416c412c974'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from A.blog import routes