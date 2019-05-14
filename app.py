from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tabledef import *
import json
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def index():
    query = session.query(Flashcard).all()
    data = []
    for obj in query:
        data.append({'term': obj.term, 'definition': obj.definition}) 
    return render_template('index.html', data=data)

    return 'hello'

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)

