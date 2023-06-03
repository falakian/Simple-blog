from flask import render_template
from blog import app
from blog.forms import RegistrationForm , LoginForm

@app.route("/")
def Home():
    return render_template('home.html')


def register():
    form = RegistrationForm()
    return render_template('register.html' , form=form)