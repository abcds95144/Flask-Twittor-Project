import os
from flask import Flask
from twittor.route import index, login
from dotenv import load_dotenv


load_dotenv()  # 讀取 .env

def create_app():

    app=Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'fallback-secret-key'
    app.add_url_rule('/','index',index)
    app.add_url_rule('/login','login',login, methods=['GET','POST'])
    return app