from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)
#app.config['SQLA']

from blog import routes
