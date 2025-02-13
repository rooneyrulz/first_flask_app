from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import (
  DataRequired,
  Length,
  Email,
  EqualTo,
  ValidationError
)
from first_flask_app.models import User


class RegisterForm(FlaskForm):
  username = StringField(
    'Username',
    validators=[DataRequired(), Length(min=2, max=20)]
  )
  email = StringField(
    'Email',
    validators=[DataRequired(), Email()]
  )
  password = PasswordField(
    'Password',
    validators=[DataRequired()]
  )
  confirm_password = PasswordField(
    'Confirm Password',
    validators=[DataRequired(), EqualTo('password')]
  )
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('Username has already been taken!')
    else:
      return username

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('Email has already been taken!')
    else:
      return email


class LoginForm(FlaskForm):
  email = StringField(
    'Email',
    validators=[DataRequired(), Email()]
  )
  password = PasswordField(
    'Password',
    validators=[DataRequired()]
  )
  remember = BooleanField('Remember Me')
  submit = SubmitField('Log In')

