from flask import Flask, jsonify
from app.config import Config
from app.extensions import db
from flask import Blueprint, jsonify
from app.models import User
from app.blueprints.api.routes import api

api = Blueprint("api", __name__)

@api.route("/users")
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)
    
    app.register_blueprint(api, url_prefix="/api")
    
    from app.blueprints.main import main
    app.register_blueprint(main)
    
    from app.blueprints.admin import admin
    app.register_blueprint(admin)
    
    from app.blueprints.auth import auth
    app.register_blueprint(auth)
    
    
    return app