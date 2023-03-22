from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    email = StringField("email", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
    submit = SubmitField("Login")