from flask import render_template
from settings import app, db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash


migrate = Migrate(app, db)

#Make sure to set FLASK_APP=app.py
import models

def addUser(u, r, p):
    user = models.User(username=u, role=r, password_hash=generate_password_hash(p))
    db.session.add(user)
    db.session.commit()

def addPost(b, t, i, d, u):
    post = models.BlogObject(blogType=b, title=t, image=i, description=d, user=u)
    db.session.add(post)
    db.session.commit()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return '<h1>Login Page under construction</h1>'

@app.route('/newPost', methods=['GET', 'POST'])
def post():
    return '<h1>This Page will be a new post form</h1>'

@app.route('/newAdmin')
def admin():
    return '<h1>This page will allow registeration of new admin</h1>'

@app.route('/blog/<blogType>')
def blog(blogType):
    posts = models.BlogObject.query.all()
    return render_template('blogDisplay.html', blogType=blogType, posts=posts)

if __name__=='__main__':
    app.run(debug=True, port=8080)