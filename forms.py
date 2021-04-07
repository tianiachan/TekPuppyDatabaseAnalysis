from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    size = StringField('Size of Puppy (small, medium, large):')
    age = IntegerField('Age of Puppy (years):')
    breed = StringField('Breed of Puppy:')
    activity_mode = StringField('Activity mode (couch potato, regular, hyper):')
    submit = SubmitField('Add Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Foster Pawrent:')
    pup_id = IntegerField("Id of Puppy: ")
    email = StringField('Email: ')
    submit = SubmitField('Add Foster Pawrent')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Adopted Puppy:')
    submit = SubmitField('Remove Adopted Puppy')
