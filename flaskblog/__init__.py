from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.secret import secret

app = Flask(__name__)
app.config['SECRET_KEY'] = secret
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes 
'''
This is kept after line 7 to prevent circular import
'''