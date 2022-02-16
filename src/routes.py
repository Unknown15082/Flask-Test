from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from src import app
from src.forms import LoginForm
from src.models import User

# Debugging purposes only
user = {'username': 'Unknown1508', 'displayname': 'Unknown'}
blogs = [
    {
        'author_id': 1,
        'content': 'Some random content'
    },
    {
        'author_id': 2,
        'content': 'Extra random stuff'
    },
    {
        'author_id': 1,
        'content': 'Just testing debug mode'
    }
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', blog_list = blogs)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already logged in.')
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if (user is None) or (not user.check_password(form.password.data)):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        else:
            login_user(user, remember = form.stay_login.data)
            return redirect(url_for('index'))

    return render_template('login.html', title = 'Login', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))