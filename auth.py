from flask import Blueprint, flash, render_template, url_for, request, redirect
#from werkzeug.security import generate_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return 'use this to log out'

@auth.route('/remove-student/<id>', methods=['POST'])
def remove_student_post(id):

    user = User.query.filter_by(id=id).first()

    print("Deleting user")
    print(id)

    #can't have more than one person with the same ID
    if user:
        print("removing", user.name, user.id, user.points)
        db.session.delete(user)
        db.session.commit()
        flash("User deleted")
    else:
        return "Error, user doesn't exist"

    return redirect(url_for('main.index'))

@auth.route('/update-students', methods=['POST'])
def update_student_post():

    for user in User.query:
        print("points-input"+str(user.id))
        points = request.form.get("points-input"+str(user.id))
        print("points: " + str(points))
        if(user.points != points):
            user.points = points
            db.session.commit()

    return redirect(url_for('main.index'))

@auth.route('/add-student', methods=['POST'])
def add_student_post():
    name = request.form.get('name-input') #The name in the html doccument determines where to get from
    id = request.form.get('id-input')
    points = request.form.get('points-input')

    print(name, id, points)

    user = User.query.filter_by(id=id).first()

    #can't have more than one person with the same ID
    if user:
        print("This ID already exists")
        return "Error, this ID already exists"

    new_user = User(id=id, name=name, points=points)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('main.index'))