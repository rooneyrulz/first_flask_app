from flask import render_template, flash, redirect, url_for
from first_flask_app.forms import RegisterForm, LoginForm
from first_flask_app.models import User, Post
from first_flask_app import app, db, bcrypt

@app.route('/')
def index():
  return render_template('home/index.html', title='Home')

@app.route('/about')
def about():
  return render_template('about/about.html', title='About')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard/dashboard.html', title='Dashboard')

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(
      username=form.username.data,
      email=form.email.data,
      password=hashed_pwd
    )
    db.session.add(user)
    db.session.commit()
    flash(f"Account has been created successfully, Let's login!", 'success')
    return redirect(url_for('login'))
  return render_template('auth/register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'ruzny@ruzny.com' and form.password.data == 'ruzny':
      flash(f'Welcome, You have been logged in!', 'success')
      return redirect(url_for('dashboard'))
    else:
      flash('Oops, Invalid Credentials!', 'danger')
  return render_template('auth/login.html', title='Log In', form=form)

@app.route('/posts')
def posts():
  return render_template('posts/posts.html', title='Posts', posts='posts')

@app.route('/posts/create', methods=['GET', 'POST'])
def posts_create():
  return render_template('posts/posts_create.html', title='Create Posts')
