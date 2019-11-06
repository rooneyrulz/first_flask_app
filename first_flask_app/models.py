from first_flask_app import db
from datetime import datetime


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __repr__(self):
    return self.username


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
  created_at = db.Column(
    db.DateTime,
    nullable=False,
    default=datetime.utcnow
  )

  def __repr__(self):
    return self.title
