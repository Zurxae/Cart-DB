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


class EditInfoForm(FlaskForm):
    fname = StringField('First Name', [validators.DataRequired()])
    lname = StringField('Last Name', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])
    zipcode = IntegerField('Zip Code', [validators.DataRequired()])
    state = StringField('State', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])
    submit = SubmitField("Submit")


class MenuForm(FlaskForm):
    chicken_tenders = IntegerField('Chicken Tenders ($4.00)', [validators.NumberRange(min=0)], default=0)
    coke = IntegerField('Coke ($1.20)', [validators.NumberRange(min=0)], default=0)
    hamburger = IntegerField('Hamburger ($5.50)', [validators.NumberRange(min=0)], default=0)
    hot_dog = IntegerField('Hot Dog ($4.75)', [validators.NumberRange(min=0)], default=0)
    pepsi = IntegerField('Pepsi ($1.20)', [validators.NumberRange(min=0)], default=0)
    water = IntegerField('Water ($0.50)', [validators.NumberRange(min=0)], default=0)
    submit = SubmitField("Checkout")

class CheckoutForm(FlaskForm):
    card_number = IntegerField('Card Number', [validators.DataRequired()])
    cvc = IntegerField('CVC', [validators.DataRequired()])
    submit = SubmitField("Confirm Order")