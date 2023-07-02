import dash
import dash_bootstrap_components as dbc
import sqlite3
from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import os

conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')
db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

Users_tbl = Table('users', Users.metadata)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
server = app.server
app.config.suppress_callback_exceptions = True

server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False)

db.init_app(server)

class Users(UserMixin, Users):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        # Implement your own logic to return a unique identifier for the user
        return self.username

# Setup the LoginManager for the server
