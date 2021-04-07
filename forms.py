from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    weight = IntegerField('Weight of Puppy:')
    age = IntegerField('Age of Puppy:')
    coat_color = StringField('Coat Color of Puppy:')
    submit = SubmitField('Add Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Foster Pawrent:')
    pup_id = IntegerField("Id of Puppy: ")
    email = StringField('Email: ')
    submit = SubmitField('Add Foster Pawrent')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Adopted Puppy:')
    submit = SubmitField('Remove Adopted Puppy')
