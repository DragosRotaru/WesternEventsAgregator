from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Source, SuggestedSource, Event

app = Flask(__name__)

engine = create_engine('sqlite:///Westernevents.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/index.html')
def index():
    events = session.query(Event).all()
    sources = session.query(Source).all()
    # return ""
    return render_template('index.html', events=events, sources=sources)


@app.route('/api/v1.0/events', methods=['GET'])
def getevents():
    return jsonify({'events': tasks})

@app.route('/email')
@app.route('/email.html')
def showemailpage():
    # return "This will display the websites email page"
    return render_template('email.html')



@app.route('/addevent')
@app.route('/addevent.html')
def showaddeventpage():
    # return "This will display the websites about page"
    return render_template('addevent.html')

@app.route('/addlink')
@app.route('/addlink.html')
def showaddlinkpage():
    # return "This will display the websites about page"
    return render_template('addlink.html')

@app.route('/addsource')
@app.route('/addsource.html')
def showaddsourcepage():
    # return "This will display the websites about page"
    return render_template('addsource.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
