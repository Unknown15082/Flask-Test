from src import app
from src.forms import LoginForm
from src.models import User

from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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
            next_page = request.args.get('next')
            if (next_page is None) or (url_parse(next_page).netloc != ''):
                return redirect(url_for('index'))
            return redirect(next_page)

    return render_template('login.html', title = 'Login', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/write', methods = ['GET', 'POST'])
@login_required
def write():
    return render_template('write.html', title = 'Write a blog')