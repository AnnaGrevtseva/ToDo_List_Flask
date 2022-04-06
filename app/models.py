"""Module to create database and app"""

import os

from app.settings import settings
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.track_modifications
db = SQLAlchemy(app)


# pylint: disable=too-few-public-methods
class Todo(db.Model):
    """To do database model"""

    # pylint: disable=no-member
    task_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

    def __init__(self, text: str, complete):

        self.text = text
        self.complete = complete

    def __repr__(self):
        return f'<sleep {self.text}>'
