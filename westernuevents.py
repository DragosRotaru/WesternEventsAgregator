from flask import Flask, render_template, request, redirect, jsonify, url_for
from forms import *

app = Flask(__name__)
app.config.from_object('config')

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
    return render_template('shareevent.html', form=form)

@app.route('/sharelink', methods=['GET', 'POST'])
@app.route('/sharelink.html', methods=['GET', 'POST'])
def showsharelinkpage():
    # return "Display ShareLinkForm"
    form = ShareLinkForm()
    return render_template('sharelink.html', form=form)

@app.route('/sharesource', methods=['GET', 'POST'])
@app.route('/sharesource.html', methods=['GET', 'POST'])
def showsharesourcepage():
    # return "Display ShareSourceForm"
    form = ShareSourceForm()
    return render_template('sharesource.html', form=form)

if __name__ == '__main__':
    app.run(debug=True) #app.run(host = '0.0.0.0')
