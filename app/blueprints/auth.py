from flask import Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/user/<username>')

def profile(username):
    return f"Hello, {username}! This is your profile."