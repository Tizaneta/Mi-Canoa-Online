from flask import Blueprint
progress = Blueprint('progress', __name__)

@progress.route('/progress')
def show_progress():
    return "This is the progress page for Canoa Online."