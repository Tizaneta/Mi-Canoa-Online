from flask import Blueprint, jsonify
from app.models import User

api = Blueprint("api", __name__)

@api.route("/users")
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@api.route("/users/<int:id>")
def get_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict())