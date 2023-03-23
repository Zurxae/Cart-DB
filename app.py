from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import LoginForm, SignUpForm, EditInfoForm, MenuForm
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
    
    form = EditInfoForm(fname=values[0], lname=values[1], address=values[2], zipcode=values[3], state=values[4], city=values[5])

    if form.validate_on_submit():
        passed = editUserInfo(form, config, session['email'])
        
        if passed:
            return redirect(url_for('menu'))
    return render_template('edit-info.html', form = form)

@app.route('/menu/', methods=['GET', 'POST'])
def menu():
    form = MenuForm()
    print('1')
    if form.validate_on_submit():
        print("2")
        menuOrder = [form.chicken_tenders.data, form.coke.data, form.hamburger.data, form.hot_dog.data, form.pepsi.data, form.water.data,]
        print(menuOrder)
        return redirect(url_for('checkout'))
    return render_template('menu.html', form=form)  

@app.route('/checkout/')
def checkout():
    return render_template('checkout.html')

