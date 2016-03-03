from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from views import *
from models import *

if __name__ == '__main__':
    if app.config['ENV'] == 'DEV':
        app.run(debug=True)
    if app.config['ENV'] == 'PROD':
        app.run(host = '0.0.0.0')
