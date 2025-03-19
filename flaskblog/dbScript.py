from flaskblog import db
from flaskblog.models import User, Post
from flaskblog import app
from datetime import datetime
with app.app_context():
    # db.create_all()
    
    all = User.query.all()
    print(type(all))
    for some in all:
        print(some)
    
    # user = User.query.filter_by(username='Pranav1').first()
    # if user:
    #     print(user.password)
    
    # user = User.query.filter_by(username='Pranav').first()
    # user1 = User.query.filter_by(username='Pranav1').first()
    # user2 = User.query.filter_by(username='Pranav2').first()
    # if user:
    #     db.session.delete(user)
    #     db.session.delete(user1)
    #     db.session.delete(user2)
    #     db.session.commit()
    
    # posts = Post.query.paginate(per_page=2, page=3)
    # # for post in posts:
    # #     print(post)
    # # print(posts.per_page)
    # # print(posts.page)
    # for post in posts.iter_pages():
    #     print(post)
    
    # posts = Post.query.all()
    # for post in posts:
    #     # post.date_posted = datetime.now()
    #     print(post)
    # # db.session.commit()
    
    # user = User.query.filter_by(username='Pranavv').first()
    # if user:
    #     print(user.password)