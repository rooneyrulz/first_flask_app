from flask import Flask, render_template

app = Flask(__name__)

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
  return render_template('auth/register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('auth/login.html', title='Log In')

@app.route('/posts')
def posts():
  return render_template('posts/posts.html', title='Posts', posts='posts')

@app.route('/posts/create', methods=['GET', 'POST'])
def posts_create():
  return render_template('posts/posts_create.html', title='Create Posts')

if __name__ == '__main__':
  app.run(debug=True)
