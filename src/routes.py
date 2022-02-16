from flask import render_template
from src import app

# Debugging purposes only
user = {'username': 'Unknown1508', 'displayname': 'Unknown'}
ratinglist = [
    {
    'user': user,
    'rating': 2278
    }
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', ratinglist = ratinglist)