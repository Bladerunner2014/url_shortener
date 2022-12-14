from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '2493020c05bc64c07f6bedc8e21c9fc4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../shorty.db'
app.app_context().push()
db = SQLAlchemy(app)

from urlsrtner import routes
