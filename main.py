from flask import Blueprint, render_template

from CMSC447_HW1.models import User

#Blueprint used to organize files in flask project
main = Blueprint('main', __name__)

#'/' means the home route
@main.route('/', methods = ['GET'])
def index():

    users = User.query.order_by(User.id)
    return render_template('table.html', users = users)

@main.route('/update', methods = ['GET'])
def update():
    users = User.query.order_by(User.id)
    return render_template('update_table.html', users = users)

@main.route('/profile')
def profile():
    return render_template('profile.html')