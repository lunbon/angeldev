from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField
from wtforms.validators import DataRequired

class EditForm(FlaskForm):
	header = StringField('header', validators=[DataRequired()])
	body = TextAreaField('body', validators=[DataRequired()])
	url = StringField('url', validators=[DataRequired()])
	submit=SubmitField()

class EditChapterForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	description = TextAreaField('description', validators=[DataRequired()])
	number = IntegerField('number', validators=[DataRequired()])
	url = StringField('url')
	submit=SubmitField()