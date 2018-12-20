from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Student:')
    submit = SubmitField('Add Student')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Student to Remove:')
    submit = SubmitField('Remove Student')
