from flask import render_template, redirect, request, url_for
from twittor.form import LoginForm
from twittor.models import User, Tweet

def index(): 
    name={'username':'root'} 
    posts= [
        {
            'author':{'username':'root'},
            'body':"hi I'm test!"
        },
        {
            'author':{'username':'test'},
            'body':"hi I'm test!"
        }

    ]
    return render_template('index.html',name=name,posts=posts)

#def login():
 #   form = LoginForm(csrf_enabled=False)
  #  if form.validate_on_submit
   #     return redirect('/')
    #return render_template('login.html', title="Sign In", form=form)


def login():
    form = LoginForm(request.form, csrf_enabled=False)

    if request.method == 'POST':
        print("POST 收到！")
        print("username:", form.username.data)
        print("password:", form.password.data)
        print("remember_me:", form.remember_me.data)
        return redirect(url_for('index'))  # 強制跳轉首頁

    return render_template('login.html', title="Sign In", form=form)