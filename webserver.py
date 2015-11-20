from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Source, SuggestedSource, Event

app = Flask(__name__)

engine = create_engine('sqlite:///Westernevents.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show Main page
@app.route('/')
@app.route('/index.html')
def showmainpage():
    events = session.query(Event).all()
    sources = session.query(Source).all()
    # return "This page will show all my sources"
    return render_template('index.html', events=events, sources=sources)

@app.route('/about')
@app.route('/about.html')
def showaboutpage():
    # return "This will display the websites about page"
    return render_template('about.html')

@app.route('/home')
@app.route('/home.html')
def showhomepage():
    # return "This will display the websites about page"
    return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
