import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_mail import Mail
from twittor.config import Config
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'login'
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    from twittor.route import index, login, logout, register, user, page_not_found, edit_profile, reset_password_request, password_reset, toggle_like
    app.add_url_rule('/index', 'index',  methods=['GET','POST'])
    app.add_url_rule('/', 'index', index, methods=['GET','POST'])
    app.add_url_rule('/login', 'login', login, methods=['GET','POST'])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/register', 'register', register, methods=['GET','POST'])
    app.add_url_rule('/<username>', 'profile', user, methods=['GET','POST'])
    app.add_url_rule('/edit_profile', 'edit_profile', edit_profile, methods=['GET','POST'])
    app.add_url_rule('/reset_password_request', 'reset_password_request', reset_password_request, methods=['GET','POST'])
    app.add_url_rule('/password_reset/<token>', 'password_reset', password_reset, methods=['GET','POST'])
    app.add_url_rule('/api/like/<int:id>', 'toggle_like', toggle_like, methods=['POST'])
    app.register_error_handler(404, page_not_found)
   
    from . import models

    return app