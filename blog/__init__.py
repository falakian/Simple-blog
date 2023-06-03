from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)
app.config['SECRET_KEY'] = '04edbb5c1ca8ba4b6351d416c412c974'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../blog.db"
db = SQLAlchemy(app)
from blog import routes