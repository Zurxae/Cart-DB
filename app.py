from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import LoginForm, SignUpForm
from widgets.authUser import authUser
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
        return redirect(url_for('menu'))
    return render_template('sign-up.html', form = form)

@app.route('/editinfo/')
def editInfo():
    return render_template('edit-info.html')

@app.route('/menu/')
def menu():
    return render_template('menu.html')

@app.route('/checkout/')
def checkout():
    return render_template('checkout.html')






# refresh_db = "DROP TABLE IF EXISTS users"
# cursor.execute(refresh_db)

# create = """
# CREATE TABLE users (
#     email VARCHAR(50) NOT NULL,
#     password VARCHAR(50) NOT NULL,
#     fname VARCHAR(50) DEFAULT '' NOT NULL,
#     lname VARCHAR(50) DEFAULT '' NOT NULL,
#     PRIMARY KEY(email)
# ) ENGINE=InnoDB"""

# cursor.execute(create)