from flask.ext.wtf import Form
from flask.ext.wtf.recaptcha import RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired, URL

class ShareSourceForm(Form):
	url = StringField('URL', validators=[DataRequired(), URL()])
	recaptcha = RecaptchaField()

class ShareLinkForm(Form):
	url = StringField('URL', validators=[DataRequired(), URL()])
	recaptcha = RecaptchaField()

class ShareEventForm(Form):
	title = StringField('Title', validators=[DataRequired()])
	url = StringField('URL', validators=[DataRequired(), URL()])
	recaptcha = RecaptchaField()
