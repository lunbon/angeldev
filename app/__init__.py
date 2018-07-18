from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_migrate import Migrate
from flask_misaka import Misaka

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'index'
Misaka(app, escape=True, wrap=True)

from app.titles import titles
from app.posts import posts
from app.auth import auth
from app.moder import moder

app.register_blueprint(titles, url_prefix='/releases')
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(moder, url_prefix='/moder')

from app import routes