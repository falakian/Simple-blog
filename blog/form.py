from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField , SubmitField 
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from blog.models import User
from flask_login import current_user
class RegistrationForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() ,
                                        Length( min =4 , max = 30 , message ='Username must be between 4 and 25 characters') ])
    email = StringField('Email' , validators=[DataRequired() , Email( message ='The email entered is invalid')])
    password = PasswordField('Password' , validators=[DataRequired()])
    confirm_password = PasswordField ('Confirm password' , validators=
                                    [DataRequired(),EqualTo('password' , message='Repeating the password is wrong')] )
    submit = SubmitField('register')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already registered')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already registered')
        

class LoginForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() ,
                                        Length( min =4 , max = 30 , message ='Username must be between 4 and 25 characters') ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('login')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() ,
                                        Length( min =4 , max = 30 , message ='Username must be between 4 and 25 characters') ])
    email = StringField('Email' , validators=[DataRequired() , Email( message ='The email entered is invalid')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is already registered')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is already registered')