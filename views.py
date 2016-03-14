from flask import render_template, request, redirect, jsonify, url_for, flash
from app import app
from forms import *

@app.route('/')
@app.route('/index.html')
def index():
    # return "Display the main page"
    return render_template('index.html')


@app.route('/api/events', methods=['GET'])
def getevents():
    #return "Provide event information"
    return jsonify({'events': 'TODO'})

@app.route('/email')
@app.route('/email.html')
def showemailpage():
    # return "Display newsletter signup"
    return render_template('email.html')

@app.route('/share', methods=['GET', 'POST'])
@app.route('/share.html', methods=['GET', 'POST'])
def showshareeventpage():
    # return "Display ShareEventForm"
    form = ShareEventForm()
    if form.validate_on_submit():
        flash('Event Shared: %s' % (form.title.data))
        return redirect('/')
    return render_template('share.html', form=form)
