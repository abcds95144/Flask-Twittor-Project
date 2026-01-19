import os

config_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'twittor.db'))
    SECRET_KEY = os.getenv('SECRET_KEY') or 'fallback-secret-key'
    SECRET_KEY = 'abc123'