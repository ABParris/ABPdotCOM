from flask import render_template
from settings import app, db
from flask_migrate import Migrate


migrate = Migrate(app, db)

#Make sure to set FLASK_APP=app.py
import models

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return '<h1>Login Page under construction</h1>'

@app.route('/blog/<blogType>')
def blog(blogType):
    user = models.User(username='Admin', role='admin', password_hash='')
    db.session.add(user)
    db.session.commit()
    user = models.User.query.get(1)
    print(user)
    post3 = models.BlogObject(blogType='research', title='post three', image='image', description='Just a short discription', user=user)
    post4 = models.BlogObject(blogType='research', title='post four', image='image', description='Just a short discription about the post', user=user)
    post5 = models.BlogObject(blogType='research', title='post five', image='image', description="let's see if this string appears", user=user)
    post6 = models.BlogObject(blogType='research', title='post six', image='image', description="let's see if this string appears", user=user)
    post7 = models.BlogObject(blogType='research', title='post seven', image='image', description="let's see if this string appears", user=user)
    db.session.add(post7)
    db.session.add(post4)
    db.session.commit()
    post8 = models.BlogObject(blogType='research', title='post eight', image='image', description="let's see if this string appears", user=user)
    posts = models.BlogObject.query.all()
    print(posts)
    return render_template('blogDisplay.html', blogType=blogType, posts=posts)

if __name__=='__main__':
    app.run(debug=True, port=8080)