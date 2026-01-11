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

    # 使用絕對路徑生成資料庫，保證在專案根目錄
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'twittor.db')}"
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'fallback-secret-key'

    db.init_app(app)
    migrate.init_app(app, db)

    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=['GET','POST'])

    # ✅ import models 確保 Alembic 可以找到 table
    from . import models

    return app