from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, URL

class SuggestedSourceForm(Form):
	url = StringField('URL', validators=[DataRequired(), URL()])

class SuggestedLinkForm(Form):
	url = StringField('URL', validators=[DataRequired(), URL()])

class SuggestedEventForm(Form):
	title = StringField('Title', validators=[DataRequired()])
	url = StringField('URL', validators=[DataRequired(), URL()])
