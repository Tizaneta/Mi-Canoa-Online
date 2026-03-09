from flask import Blueprint 

admin = Blueprint('admin', __name__)
@admin.route('/admin/dashboard')
def dashboard():
    return 'Admin Dashboard'