from flask import Flask, render_template, flash, redirect, url_for
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '157e035b48b7865868e7169fab329fd79b1'

posts = [
  {
    'title':'Some Title'
  },
  {
    'title':'Another Title'
  }
]

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
    flash(f'Account has been created for {form.username.data}!', 'success')
    print('success')
    return redirect(url_for('dashboard'))
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

if __name__ == '__main__':
  app.run(debug=True)
