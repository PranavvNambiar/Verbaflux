from flaskblog import db
from flaskblog.models import User, Post
from flaskblog import app
with app.app_context():
    # db.create_all()
    all = User.query.all()
    for some in all:
        print(some)
    user = User.query.first()
    print(user.password)