from flaskblog import db
from flaskblog.models import User, Post
from flaskblog import app
with app.app_context():
    # db.create_all()
    print(User.query.all())