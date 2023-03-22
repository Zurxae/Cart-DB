from flask import Flask, render_template
#import mysql.connector

app = Flask(__name__)

@app.route('/')
@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def login():
    return render_template('sign-up.html')

@app.route('/editinfo/')
def login():
    return render_template('edit-info.html')

@app.route('/menu/')
def login():
    return render_template('menu.html')

@app.route('/checkout/')
def login():
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