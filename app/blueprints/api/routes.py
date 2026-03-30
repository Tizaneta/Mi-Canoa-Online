from flask import Blueprint, jsonify, request
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

@api.route("/users", methods=["POST"])
def create_user():
    data = request.json
    
    if not data or not data.get("username") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "faltan datos"}), 400
    user = User(
        username=data["username"],
        email=data.get("email"),
        password=data.get("password")
    )

    from app.extensions import db
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201