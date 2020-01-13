from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/blog/<blogType>')
def blog(blogType):
    print(blogType)
    return render_template('blogDisplay.html')

if __name__=='__main__':
    app.run(debug=True, port=8080)