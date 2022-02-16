from flask import render_template
from src import app
from src.forms import LoginForm

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)