from flask import render_template , redirect , url_for
from blog import app , db , bcrypt
from A.blog.form import RegistrationForm , LoginForm
from A.blog.models import User , Post

@app.route("/" , methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hased_pass)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html' , form=form)
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html' , form=form)