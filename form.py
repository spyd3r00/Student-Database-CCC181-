from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired, Length

class AddForm(FlaskForm):
	fullName = StringField('Full Name',validators=[DataRequired(), Length(min = 8, max = 30)])
	Course = SelectField('Course',choices=[('BSCS','BSCS'),('BSMATH','BSMATH'),('DTTE','DTTE'),('BSCE','BSCE'),('BSPSYCH','BSPSYCH'),('BSBA','BSBA'),('NURSING','NURSING')])
	idNumber = StringField('ID Number',validators=[DataRequired(), Length(min = 9, max = 9)])
	year = SelectField('Year ',choices=[('1','1'),('2','2'),('3','3'),('4','4')])
	gender = SelectField('Gender ',choices=[('Male','Male'),('Female','Female')])
	submit = SubmitField('Add Students')
	edit = SubmitField ('Complete Changes')

class searchForm(FlaskForm):
	key = StringField('ID Number',validators=[DataRequired(), Length(min = 2, max = 9)])
	SubmitField = SubmitField('Search')