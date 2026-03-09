from flask import Flask
from app.config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)
    
    from app.blueprints.main import main
    app.register_blueprint(main)
    
    from app.blueprints.admin import admin
    app.register_blueprint(admin)
    
    from app.blueprints.auth import auth
    app.register_blueprint(auth)
    
    return app