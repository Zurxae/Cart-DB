#from flask import Flask
import mysql.connector

#app = Flask(__name__)

# @app.route('/')
# def hello():
#     return '<h1>Hello, World!</h1>'


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

db = mysql.connector.Connect(**config)
cursor = db.cursor()

refresh_db = "DROP TABLE IF EXISTS users"
cursor.execute(refresh_db)

create = """
CREATE TABLE users (
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    fname VARCHAR(50) DEFAULT '' NOT NULL,
    lname VARCHAR(50) DEFAULT '' NOT NULL,
    PRIMARY KEY(email)
) ENGINE=InnoDB"""

cursor.execute(create)