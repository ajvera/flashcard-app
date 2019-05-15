import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file =  "postgresql://avera:@+0Ku$@@localhost/flashapp".format(os.path.join(project_dir, "flashapp.db"))
database_file =  "postgres://dfrjqzdijhpkgb:b1dc57010e2284d7f59edd034651d5302115d490265bd6e9faed14991bee4863@ec2-75-101-147-226.compute-1.amazonaws.com:5432/d3bb19dj0l1lk1".format(os.path.join(project_dir, "flashapp.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Flashcard(db.Model):
    flashcardID = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    term = db.Column(db.String(256), unique=False, nullable=False)
    definition = db.Column(db.String(256), unique=False, nullable=False)