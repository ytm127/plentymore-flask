from app import app, db
from app.models import User, Post

# create shell configuration here. This is optional but is helpful 
@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}