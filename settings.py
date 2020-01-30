import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'alskdjfasfieaohlkafjsdlkfhoaiasdfasd'
db = SQLAlchemy(app)