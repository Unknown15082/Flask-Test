from flask import render_template
from src import app

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
    }
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', blog_list = blogs)