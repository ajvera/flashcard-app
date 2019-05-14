from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tabledef import *
import json
from pprint import pprint

app = Flask(__name__)

#Homepage will eventually direct users to their preffered learning style
@app.route("/")
def index():
    session.rollback()
    return render_template('index.html')

#Flashcard review page
@app.route("/flashcards")
def get():
    query = session.query(Flashcard).all()
    data = []
    for obj in query:
        data.append({'id': obj.flashcardID, 'term': obj.term, 'definition': obj.definition})
    return render_template('show.html', data=data)

#Create new flashcard
@app.route("/flashcards/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        flashcard = Flashcard(term=request.form['term'], definition=request.form['definition'])
        session.add(flashcard)
        session.commit()
        return redirect('/flashcards')
    
    return render_template('new.html')

#Update an existing flashcard
@app.route("/flashcards/update/<id>", methods=["GET","POST"])
def update(id):
    flashcard = session.query(Flashcard).get(id)
    print(Flashcard)
    
    
    if request.method == "POST":
        session.query(Flashcard).filter(id).update(term=request.form["term"], definition=request.form['definition'])
        session.commit()
        return redirect('show.html')

    return render_template('update.html', flashcard=flashcard)

@app.route("/flashcards/delete")
def delete():
    query = session.query(Flashcard).all()
    data = []
    for obj in query:
        data.append({'term': obj.term, 'definition': obj.definition}) 
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)

