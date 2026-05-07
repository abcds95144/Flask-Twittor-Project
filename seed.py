from twittor import create_app, db
from twittor.models import User, Tweet


app = create_app()
app.app_context().push()
User.query.all()

app = create_app()


with app.app_context():
    print("START")
    db.drop_all()
    db.create_all()

    u1 = User(username="admin", email="admin@admin.com", about_me="I love Flask")
    u1.set_password("admin")

    u2 = User(username="demo", email="demo@demo.com", about_me="Hello world")
    u2.set_password("demo")

    u3 = User(username="demo2", email="demo2@test.com", about_me="I'm admin")
    u3.set_password("demo2")

    u4 = User(username="test", email="test@test.com", about_me="I'm test")
    u4.set_password("test")

    db.session.add_all([u1, u2, u3])
    db.session.commit()

 
    t1 = Tweet(body="Hello from John!", author=u1)
    t2 = Tweet(body="Mary's first post!", author=u2)
    t3 = Tweet(body="Admin here 👀", author=u3)
    t4 = Tweet(body="Another post from John", author=u1)

    db.session.add_all([t1, t2, t3, t4])
    db.session.commit()

    print("THIS FILE:", __file__)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    
    