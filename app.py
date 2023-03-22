from flask import Flask, render_template, request, flash, redirect, url_for
from forms import LoginForm
#import mysql.connector

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for('menu'))
    return render_template('login.html', form = form)
        

@app.route('/signup/')
def signUp():
    return render_template('sign-up.html')

@app.route('/editinfo/')
def editInfo():
    return render_template('edit-info.html')

@app.route('/menu/')
def menu():
    return render_template('menu.html')

@app.route('/checkout/')
def checkout():
    return render_template('checkout.html')


# config = {
#     "host": "localhost",
#     "port": 3306,
#     "database": "cart",
#     "user": "root",
#     "password": "root",
#     "charset": "utf8",
#     "use_unicode": True,
#     "get_warnings": True,
# }

# db = mysql.connector.Connect(**config)
# cursor = db.cursor()

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