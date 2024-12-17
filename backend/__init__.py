from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize the db object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Set your app configuration (add your configuration here)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with the app
    db.init_app(app)

    # Import and register blueprints
    from backend.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
