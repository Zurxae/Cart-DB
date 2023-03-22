from flask_wtf import FlaskForm
from wtforms import (Form, StringField, PasswordField, IntegerField, SubmitField, validators)


class LoginForm(FlaskForm):
    email = StringField("email", [validators.DataRequired()])
    password = PasswordField("password", [validators.DataRequired()])
    submit = SubmitField("Login")


class SignUpForm(FlaskForm):
    email = StringField("email", [validators.DataRequired()])
    password = PasswordField("password", [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords must match')
        ])
    confirm = PasswordField('Repeat Password')
    fname = StringField('First Name', [validators.DataRequired()])
    lname = StringField('Last Name', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    zipcode = IntegerField('Zip Code', [validators.DataRequired()])
    state = StringField('State', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])
    submit = SubmitField("Submit")
