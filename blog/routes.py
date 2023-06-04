from flask import render_template , redirect , url_for , flash , request
from blog import app , db , bcrypt
from blog.form import RegistrationForm , LoginForm , UpdateProfileForm
from blog.models import User , Post
from flask_login import login_user , current_user , logout_user , login_required


@app.route("/" , methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in' , 'success' )
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hased_pass)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered','success')
        return redirect(url_for('home'))
    return render_template('register.html' , form=form)
@app.route("/login" , methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in' , 'success' )
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password , form.password.data):
            login_user(user , remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have successfully logged in' , 'success')
            return redirect(next_page if next_page else url_for('home'))
        else:
            flash('Username or password is incorrect' , 'danger')
    return render_template('login.html' , form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out' , 'success')
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/edit_profile' , methods=['GET','POST'])
@login_required
def edit_profile():
    form=UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your information has been successfully updated', 'info')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    return render_template('edit_profile.html' , form=form)
