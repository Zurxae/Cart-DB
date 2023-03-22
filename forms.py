from flask_wtf import Form
from wtforms import TextField, PasswordField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class LoginForm(Form):
    email = TextField("email", [validators.DataRequired("Please enter your email.")])
    password = PasswordField("password", [validators.DataRequired("Please enter your password.")])
    submit = SubmitField("Login")