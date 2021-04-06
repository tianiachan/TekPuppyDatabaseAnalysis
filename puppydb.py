# import os
# from forms import  AddForm , DelForm, AddOwnerForm
# from flask import Flask, render_template, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from config import username, password
# # import flask_sqlalchemy
# from flask_migrate import Migrate
# # import pyodbc
# # import sqlalchemy as sal
# # from sqlalchemy import create_engine
# # import pandas as pd
# app = Flask(__name__)
# # Key for Forms
# app.config['SECRET_KEY'] = 'mysecretkey'

# ############################################

#         # SQL DATABASE AND MODELS

# ##########################################
# basedir = os.path.abspath(os.path.dirname(__file__))
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql + pymysql://tiania:IL0v3Mochi.@localhost/puppydb'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/puppydb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# Migrate(app,db)

# class Puppy(db.Model):

#     __tablename__ = 'puppies'
#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.Text)
#     owner = db.relationship('Owner',backref='puppy',uselist=False)

#     def __init__(self,name):
#         self.name = name

#     def __repr__(self):
#         if self.owner:
#             return f"Puppy name is {self.name} and owner is {self.owner.name}"
#         else:
#             return f"Puppy name is {self.name} and has no owner assigned yet."

# class Owner(db.Model):

#     __tablename__ = 'owners'

#     id = db.Column(db.Integer,primary_key= True)
#     name = db.Column(db.Text)
#     # We use puppies.id because __tablename__='puppies'
#     puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

#     def __init__(self,name,puppy_id):
#         self.name = name
#         self.puppy_id = puppy_id

#     def __repr__(self):
#         return f"Owner Name: {self.name}"
# ############################################

#         # VIEWS WITH FORMS

# ##########################################
# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/add', methods=['GET', 'POST'])
# def add_pup():
#     form = AddForm()

#     if form.validate_on_submit():
#         name = form.name.data

#         # Add new Puppy to database
#         new_pup = Puppy(name)
#         db.session.add(new_pup)
#         db.session.commit()

#         return redirect(url_for('list_pup'))

#     return render_template('add.html',form=form)
# @app.route('/add_owner', methods=['GET', 'POST'])
# def add_owner():

#     form = AddOwnerForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         pup_id = form.pup_id.data
#         # Add new owner to database
#         new_owner = Owner(name,pup_id)
#         db.session.add(new_owner)
#         db.session.commit()

#         return redirect(url_for('list_pup'))

#     return render_template('add_owner.html',form=form)

# @app.route('/list')
# def list_pup():
#     # Grab a list of puppies from database.
#     puppies = Puppy.query.all()
#     return render_template('list.html', puppies=puppies)

# @app.route('/delete', methods=['GET', 'POST'])
# def del_pup():

#     form = DelForm()

#     if form.validate_on_submit():
#         id = form.id.data
#         pup = Puppy.query.get(id)
#         db.session.delete(pup)
#         db.session.commit()

#         return redirect(url_for('list_pup'))
#     return render_template('delete.html',form=form)


# if __name__ == '__main__':
#     app.run(debug=True)

import os
from forms import  AddForm , DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import username, password, secretKey
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = secretKey

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mys:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost/puppydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.create_all()
Migrate(app,db)

class Puppy(db.Model):
    # manually set name of table  to puppies
    __tablename__ = 'puppies'
    #create table if does not exist
    # db.create_all()
    # set column names
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    owners = db.relationship('Owner',backref='puppies',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owners:
            return f"Puppy name is {self.name} and owner is {self.owners.name}"
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet."

class Owner(db.Model):

    __tablename__ = 'owners'
    #create table if does not exist
    # db.create_all()
    #set column names
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))
    # db.create_all()

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"
db.create_all()
############################################

        # VIEWS WITH FORMS

##########################################
#home page
@app.route('/')
def index():
    return render_template('home.html')

#function to add puppy if at add puppy route
@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)

#function to add ownder if at add owner route
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html',form=form)

#display a list of the puppies and owners if it is owned by any owners
@app.route('/list')
def list_pup():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    print(puppies)
    return render_template('list.html', puppies=puppies)

#delete a puppy if no longer needed =(
@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)


#if im called main, run me
if __name__ == '__main__':
    app.run(debug=True)

