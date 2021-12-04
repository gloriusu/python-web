from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Regexp, EqualTo, ValidationError, DataRequired

from .models import User


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required'),
                                                   Length(min=4, max=25, message='Name must have greater 4 '
                                                                                 'symbol and least 25 symbol'),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Username must have only letters, numbers, '
                                                          'dots or underscores')])
    email = StringField('Email', validators=[InputRequired('Email is required'),
                                             Regexp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
                                                    message='Invalid Email')])
    password = PasswordField('Password', validators=[InputRequired('Password is required'),
                                                     Length(min=6, message='Must be at least 6')])
    confirm_password = PasswordField('Confirm password', validators=[InputRequired('Password is required'),
                                                                     Length(min=6, message='Must be at least 6'),
                                                                     EqualTo('password')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                             Regexp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Regexp('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    about_me = TextAreaField('About Me', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField(label=(''))

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is take. Please choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(username=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one')
