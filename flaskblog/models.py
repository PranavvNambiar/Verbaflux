from flask_sqlalchemy import SQLAlchemy
from authlib.jose import JsonWebSignature
import time
from flaskblog import db, loginManager,app
from flask_login import UserMixin
from datetime import datetime
import json

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"User Created('{self.username}', '{self.email}', '{self.image_file}')"
    
    def get_reset_token(self, expire=1200):
        jws = JsonWebSignature()
        header = {"alg": "HS256"}
        payload = {
            "user_id": self.id,
            "exp": int(time.time()) + expire
        }
        payload_bytes = json.dumps(payload) #* serializes a Python dict into a JSON-formatted string.
        token = jws.serialize_compact(header, payload_bytes, app.config['SECRET_KEY']) 
        return token.decode('utf-8') #! Step is very important as the token must be decoded into string to be sent into the url
    
    @staticmethod
    def verify_reset_token(token):
        jws = JsonWebSignature()
        try:
            data= jws.deserialize_compact(token, app.config['SECRET_KEY'])
            payload_dict = json.loads(data['payload'].decode('utf-8'))
            if payload_dict["exp"] < int(time.time()):  # Expired token check
                return None
            return User.query.get(payload_dict["user_id"])
        except Exception as e:
            print("Token verification error:", e)
            return None
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    '''
    ERROR - All the posts created had the same time even if created after a minute or two.
    Problem - The issue occurs because of how Python's datetime.now() is being used as a default value in your SQLAlchemy model. 
    The problem is that datetime.now() is evaluated only once when the model class is loaded, not each time a new Post is created.
    Solution - Changed the datetime.now() to datetime.now
    '''
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.now)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f"Post created: ('{self.title}', '{self.date_posted}')"
