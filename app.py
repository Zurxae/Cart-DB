from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import LoginForm, SignUpForm, EditInfoForm
from widgets.authUser import authUser
from widgets.enrollUser import enrollUser
from widgets.editUserInfo import editUserInfo
from widgets.getUserInfo import getUserInfo
#import mysql.connector

app = Flask(__name__)
app.secret_key = "secret"

config = {
    "host": "localhost",
    "port": 3306,
    "database": "cart",
    "user": "root",
    "password": "root",
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": True,
}

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        passed, email = authUser(form, config)
        
        if passed:
            session['email'] = email
            return redirect(url_for('menu'))
    return render_template('login.html', form = form)
        

@app.route('/signup/', methods = ['GET', 'POST'])
def signUp():
    form = SignUpForm()
    
    if form.validate_on_submit():
        passed, email = enrollUser(form, config)

        if passed:
            session['email'] = email
            return redirect(url_for('menu'))
    return render_template('sign-up.html', form = form)

@app.route('/editinfo/', methods = ['GET', 'POST'])
def editInfo():
    values = getUserInfo(config, session['email'])
    print(session['email'])
    print(values)
    form = EditInfoForm(fname=values[0], lname=values[1], address=values[2], zipcode=values[3], state=values[4], city=values[5])

    if form.validate_on_submit():
        passed = editUserInfo(form, config)

        if passed:
            return redirect(url_for('menu'))
    return render_template('edit-info.html', form = form)

@app.route('/menu/')
def menu():
    return render_template('menu.html')

@app.route('/checkout/')
def checkout():
    return render_template('checkout.html')

