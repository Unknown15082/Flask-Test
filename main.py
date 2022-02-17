from src import app, db
from src.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == "__main__":
    # For hosting on repl.it
    app.run(host = '0.0.0.0', port = 5000)