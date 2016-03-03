from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, URL

class ShareSourceForm(Form):
	url = StringField('URL', validators=[DataRequired(), URL()])

class ShareLinkForm(Form):
	url = StringField('URL', validators=[DataRequired(), URL()])

class ShareEventForm(Form):
	title = StringField('Title', validators=[DataRequired()])
	url = StringField('URL', validators=[DataRequired(), URL()])
