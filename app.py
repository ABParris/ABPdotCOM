from flask import render_template, url_for, request, url_for
import os
from settings import app, db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Length

migrate = Migrate(app, db)
UPLOAD_FOLDER = app.instance_path + '\static\images'
ALLOWED_EXTENSIONS = {'jpg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Make sure to set FLASK_APP=app.py
import models

class RegisterForm(FlaskForm):
    blogType = StringField('Blog Type')
    title = StringField('Title')
    description = StringField('Description')
    user = StringField('User')
    image = FileField()

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
    return render_template('login.html')

@app.route('/newPost', methods=['GET', 'POST'])
def post():
    #addPost()
    return '<h1>This Page will be a new post form</h1>'

@app.route('/newAdmin')
def admin():
    return '<h1>This page will allow registeration of new admin</h1>'

@app.route('/blog/<blogType>')
def blog(blogType):
    posts = models.BlogObject.query.all()
    return render_template('blogDisplay.html', blogType=blogType, posts=posts)

@app.route('/blogform', methods=['GET', 'POST'])
def blogform():
    
    form = RegisterForm()

    if form.validate_on_submit():
        print(""+form.blogType.data+" "+form.title.data+" "+form.description.data+" "+form.user.data+" "+form.image.data.filename)
        file = form.image.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(r'C:\Users\Alexander Parris\Desktop\Projects\Websites\ABPdotCOM\ABPdotCOM\static\images', filename))
        user = models.User.query.get(1)
        addPost(form.blogType.data, form.title.data, url_for('static', filename='images/'+filename), form.description.data, user)
        posts = models.BlogObject.query.all()
        return render_template('blogDisplay.html', blogType="whatever", posts=posts)
        return '<h1>{}</h1>'.format(filename)

    return render_template('form.html', form=form)


if __name__=='__main__':
    app.run(debug=True, port=8080)