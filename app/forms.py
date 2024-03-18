from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class Form(FlaskForm):
    name= StringField('Title', validators=[InputRequired()])
    no_of_beds= IntegerField('Number of bedrooms', validators=[InputRequired()])
    location= StringField('Location', validators=[InputRequired()])
    no_of_baths= IntegerField('Number of bathrooms', validators=[InputRequired()])
    amount= IntegerField('Price', validators=[InputRequired()])
    type= SelectField('Type', validators=[InputRequired()], choices=[('house', 'House'), ('apartment', 'Apartment')])
    description= TextAreaField('Description', validators=[InputRequired()])
    photo= FileField('image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])