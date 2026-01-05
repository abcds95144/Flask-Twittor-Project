import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twittor.route import index, login
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # ✅ 修正資料庫 URI
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///twittor.db"
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'fallback-secret-key'

    db.init_app(app)
    migrate.init_app(app, db)

    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET','POST'])

    return app
