from flask import render_template, redirect, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
from twittor.form import LoginForm
from twittor.models import User

@login_required

def index(): 
    posts = [
        {'author': {'username':'root'}, 'body':"hi I'm test!"},
        {'author': {'username':'test'}, 'body':"hi I'm test!"}
    ]
    return render_template('index.html', posts=posts)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    
    
    #print("Request method:", request.method)
    #print("Form data:", request.form)

    
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print("invalid username or password")  
            return redirect(url_for('login'))  
        print("Login success!")
        login_user(u, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if next_page:
            return redirect(next_page)
        return redirect(url_for('index'))  

    
    return render_template('login.html', title="Sign In", form=form)

def logout():
    logout_user()
    return redirect(url_for('login'))