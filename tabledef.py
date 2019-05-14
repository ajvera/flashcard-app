# from sqlalchemy import create_engine  
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base  
# from sqlalchemy.orm import sessionmaker

# db_string = "postgresql://avera:@+0Ku$@@localhost/flashapp"

# db = create_engine(db_string)
# base = declarative_base()

# class Flashcard(base):
#     __tablename__ = 'flashcards'

#     flashcardID = Column(Integer, primary_key=True)
#     term = Column(String)
#     definition = Column(String)

# Session = sessionmaker(db)  
# session = Session()

# base.metadata.create_all(db)

import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file =  "postgresql://avera:@+0Ku$@@localhost/flashapp".format(os.path.join(project_dir, "flashapp.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Flashcard(db.Model):
    flashcardID = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    term = db.Column(db.String(256), unique=False, nullable=False)
    definition = db.Column(db.String(256), unique=False, nullable=False)