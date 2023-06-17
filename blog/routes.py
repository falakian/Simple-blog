from flask import render_template , redirect , url_for , flash , request , abort
from blog import app , db , bcrypt
from blog.form import RegistrationForm , LoginForm , UpdateProfileForm , NewPostForm
from blog.models import User , Post
from flask_login import login_user , current_user , logout_user , login_required

@app.route('/')
def index():
    return redirect(url_for('home' , page=1))
@app.route("/index/<int:page>" , methods=['GET'])
def home(page=1):
    per_page=3
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page ,per_page=per_page ,error_out= True).items
    count_post = db.session.query(Post).count()
    return render_template('home.html' , posts=posts , count=count_post ,page=page)

@app.route('/api/fetch')
def count():
    count_user = db.session.query(User).count()
    return str(count_user)

@app.route("/post/<int:post_id>")
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('detail.html', post=post)

@app.route("/post/<int:post_id>/delete")
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user :
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been successfully deleted' , 'info')
    return redirect(url_for('home' , page=1))


@app.route("/post/<int:post_id>/update" , methods=['GET','POST'])
def update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user :
        abort(403)
    form = NewPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been successfully updated' , 'info')
        return redirect(url_for('detail' , post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('update.html' , form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in' , 'success' )
        return redirect(url_for('home' , page=1))
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hased_pass)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered','success')
        return redirect(url_for('home' , page=1))
    return render_template('register.html' , form=form)
@app.route("/login" , methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in' , 'success' )
        return redirect(url_for('home' , page=1))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password , form.password.data):
            login_user(user , remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have successfully logged in' , 'success')
            return redirect(next_page if next_page else url_for('home' ,page=1))
        else:
            flash('Username or password is incorrect' , 'danger')
    return render_template('login.html' , form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out' , 'success')
    return redirect(url_for('home' , page=1))

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

@app.route('/new_post' , methods=['GET','POST'])
@login_required
def new_post():
    form=NewPostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data , content=form.content.data , author =current_user )
        db.session.add(post)
        db.session.commit()
        flash('The post was created successfully' , 'success')
        return redirect(url_for('home' , page=1))
    return render_template('new_post.html' , form=form)
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403