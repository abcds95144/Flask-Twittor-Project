import os

config_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(config_path, 'twittor.db'))
    SECRET_KEY = os.getenv('SECRET_KEY') or 'c3cbeff54997958a589aef934a9dd18a98dd6bff6f2f5f0564563b6f7e4c1fc6'
    TWEET_PER_PAGE = 20

    MAIL_DEFAULT_SENDER = 'noreply@twittor.com'
    MAIL_SERVER = 'smtp.gmail.com' 
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'abcds95144@gmail.com'
    MAIL_PASSWORD = 'eswg yeno lohx iiic'
    MAIL_SUBJECT_RESET_PASSWORD = '[Twittor] Please Reset Your Password'