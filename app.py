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

# Flashcard review page
@app.route("/flashcards", defaults={'style': None})
@app.route("/flashcards/<style>")
def get(style):
    flashcards = Flashcard.query.all()
    if len(flashcards) < 1:
        flashcards = [Flashcard(term="Click me!", definition="There aren't any flashcards yet. Make some!")]
    return render_template('show.html', data=flashcards)

# Create new flashcard
@app.route("/flashcards/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        print(request.form)
        try:
            flashcard = Flashcard(term=request.form['term'], definition=request.form['definition'])
            db.session.add(flashcard)
            db.session.commit()
            redirect_url ='/flashcards'
            if request.form.get('aural'):
                redirect_url += "/aural"
            return redirect(redirect_url)
        except Exception as e:
            print("Failed to make a new flashcard, try again!")
            print(e)

    if "aural" in request.referrer:
        return render_template('new.html', referrer=request.referrer)
    
    return render_template('new.html')

# Update an existing flashcard
@app.route("/flashcards/update/<id>", methods=["GET","POST"])
def update(id):
    flashcard = Flashcard.query.get(id)

    if request.method == "POST":
        try:
            flashcard.term = request.form.get('term')
            flashcard.definition = request.form.get('definition')
            db.session.commit()
            redirect_url ='/flashcards'
            if request.form.get('aural'):
                redirect_url += "/aural"
            return redirect(redirect_url)
        except Exception as e:
            print("Failed to update the flashcard, try again!")
            print(e)

    if "aural" in request.referrer:
        return render_template('update.html', flashcard=flashcard, referrer=request.referrer)
    
    return render_template('update.html', flashcard=flashcard)

# Deletes Flashcard
@app.route("/flashcards/delete/<id>")
def delete(id):
    try:
        flashcard = Flashcard.query.get(id)
        db.session.delete(flashcard)
        db.session.commit()
        redirect_url ='/flashcards'
        if "aural" in request.referrer:
            redirect_url += "/aural"
        return redirect(redirect_url)
    except Exception as e:
        print("Failed to delete the flashcard, try again!")
        print(e)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)

