from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() ,
                                        Length( min =4 , max = 30) ])
    email = StringField('Email' , validators=[DataRequired() , Email()])
    password = PasswordField('Password' , validators=[DataRequired()])
    confirm_password = PasswordField ('Confirm password' , validators=
                                    [DataRequired(),EqualTo('password')])

class LoginForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() ,
                                        Length( min =4 , max = 30) ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')