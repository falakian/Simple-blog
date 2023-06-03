from blog import db
import datetime
class User(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(30), unique=True , nullable=False)
    email = db.Column(db.String(60),unique=True , nullable=False)
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post' , backref='author' , lazy=True)
    def __repr__(self):
        return f'User({self.id},{self.username})'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120) , nullable=False)
    date = db.Column(db.DateTime , nullable=False , default=datetime.datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)

    def __repr__(self):
        return f'Post({self.id},{self.title[:30]},{self.date})'