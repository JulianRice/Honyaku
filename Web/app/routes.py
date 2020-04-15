from app import app
from app.forms import LoginForm
from app.models import User
from flask import render_template, url_for, redirect, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    friends = [
        {
            'username':'emasuisan',
            'language':'Japanese'
        },
        {
            'username':'banri634',
            'language':'Japanese'
        },
        {
            'username':'goombajmr',
            'language':'English'
        },
        {
            'username':'priampc',
            'language':'English'
        }
    ]
    return render_template("index.html", index=True, friends=friends)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #If the user is logged in, do not allow them to stay on this page
    if (current_user.is_authenticated):
        return redirect(url_for('index'))
    
    form = LoginForm()

    #Once the form has been submitted, check the credentials
    if form.validate_on_submit():
        #Gets only one result with first()
        user = User.query.filter_by(username=form.username.data).first()

        #If queried user is not found or pw is wrong, return an error
        if user is None or not user.CheckPassword(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))

        #Let's log them in!
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/chat')
def chat():
    if not current_user.is_authenticated:
        next_page = url_for('login')
        return redirect(next_page)
    return render_template("chat.html", chat=True)

@login_required
@app.route('/talk')
def talk():
    if not current_user.is_authenticated:
        next_page = url_for('login')
        return redirect(next_page)
    return render_template("talk.html", talk=True)

@app.route('/<nm>')
def index_user(nm):
    return render_template("index.html", name=nm, index=True)
