from app import app
from app.forms import LoginForm
from flask import render_template, url_for, redirect, flash

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'kuriboX'}
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
    return render_template("index.html", index=True, user=user, friends=friends)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', form=form)

@app.route('/chat')
def chat():
    return render_template("chat.html", chat=True)

@app.route('/talk')
def talk():
    return render_template("talk.html", talk=True)

@app.route('/<nm>')
def index_user(nm):
    return render_template("index.html", name=nm, index=True)