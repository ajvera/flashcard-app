from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tabledef import *
import json
from pprint import pprint

#Homepage 
# TODO should eventually direct users to their preffered learning style
@app.route("/")
def index():
    return render_template('index.html')

#Flashcard review page
@app.route("/flashcards")
def get():
    # query = session.query(Flashcard).all()
    # data = []
    # for obj in query:
    #     data.append({'id': obj.flashcardID, 'term': obj.term, 'definition': obj.definition})
    flashcards = Flashcard.query.all()
    return render_template('show.html', data=flashcards)

#Create new flashcard
@app.route("/flashcards/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        flashcard = Flashcard(term=request.form['term'], definition=request.form['definition'])
        db.session.add(flashcard)
        db.session.commit()
        return redirect('/flashcards')
    
    return render_template('new.html')

#Update an existing flashcard
@app.route("/flashcards/update/<id>", methods=["GET","POST"])
def update(id):
    flashcard = Flashcard.query.get(id)

    if request.method == "POST":
        flashcard.term = request.form.get('term')
        flashcard.definition = request.form.get('definition')
        db.session.commit()
        return redirect('/flashcards')

    return render_template('update.html', flashcard=flashcard)

#Deletes Flashcard
@app.route("/flashcards/delete/<id>")
def delete(id):
    flashcard = Flashcard.query.get(id)
    db.session.delete(flashcard)
    db.session.commit()
    return redirect("/flashcards")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)

