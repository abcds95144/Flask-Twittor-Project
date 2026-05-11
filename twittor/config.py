import os

config_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'twittor.db'))
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-key-for-dev')
    TWEET_PER_PAGE = 20

    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_SENDER', 'noreply@twittor.com')
    MAIL_SERVER = 'smtp.gmail.com' 
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_RESET_PASSWORD = '[Twittor] Please Reset Your Password'