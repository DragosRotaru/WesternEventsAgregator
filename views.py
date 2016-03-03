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

@app.route('/shareevent', methods=['GET', 'POST'])
@app.route('/shareevent.html', methods=['GET', 'POST'])
def showshareeventpage():
    # return "Display ShareEventForm"
    form = ShareEventForm()
    if form.validate_on_submit():
        flash('Event Shared: %s' % (form.title.data))
        return redirect('/')
    return render_template('shareevent.html', form=form)

@app.route('/sharelink', methods=['GET', 'POST'])
@app.route('/sharelink.html', methods=['GET', 'POST'])
def showsharelinkpage():
    # return "Display ShareLinkForm"
    form = ShareLinkForm()
    if form.validate_on_submit():
        flash('Link Received: %s' % (form.url.data))
        return redirect('/')
    return render_template('sharelink.html', form=form)

@app.route('/sharesource', methods=['GET', 'POST'])
@app.route('/sharesource.html', methods=['GET', 'POST'])
def showsharesourcepage():
    # return "Display ShareSourceForm"
    form = ShareSourceForm()
    if form.validate_on_submit():
        flash('URL Reveived: %s' % (form.url.data))
        return redirect('/')
    return render_template('sharesource.html', form=form)
