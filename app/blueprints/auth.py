from flask import Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/user/<username>')

def profile(username):
    return f"Hi there, {username}! This is your profile from Canoa Online."