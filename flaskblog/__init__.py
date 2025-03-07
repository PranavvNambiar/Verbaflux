from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.secret import secret
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = secret
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt()
loginManager = LoginManager(app)
loginManager.login_view = 'login'
loginManager.login_message_category = 'info'

from flaskblog import routes 
'''
This is kept after line 7 to prevent circular import
'''