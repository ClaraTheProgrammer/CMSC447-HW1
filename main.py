from flask import Blueprint, render_template

#Blueprint used to organize files in flask project
main = Blueprint('main', __name__)

#'/' means the home route
@main.route('/')
def index():
    return 'Hello World!'

@main.route('/profile')
def profile():
    return "This is a profile"