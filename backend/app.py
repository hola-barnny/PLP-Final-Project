from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config
import urllib.parse

# Initialize the app
app = Flask(__name__)
app.config.from_object(Config)

# URL encode the password if it contains special characters like '@'
DB_PASSWORD = urllib.parse.quote_plus(Config.DB_PASSWORD)

# Configure the app with database and session secret
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{Config.DB_USER}:{DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"
app.config['SECRET_KEY'] = Config.SESSION_SECRET
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize CORS for handling cross-origin requests
CORS(app)

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register Blueprints
from backend.routes.auth_routes import auth_bp
from backend.routes.message_routes import message_bp  # Correctly imported without circular import
from backend.routes.meeting_routes import meeting_bp  # Correctly imported without circular import

# Register the blueprints with appropriate URL prefixes if needed
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(message_bp, url_prefix='/messages')
app.register_blueprint(meeting_bp, url_prefix='/meetings')

# Sample Route
@app.route("/")
def index():
    return jsonify({"message": "Parent-Teacher Communication App is running!"})

# Error handling routes
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"message": "Internal Server Error"}), 500

# Importing models (ensure your models are in the models folder)
from backend.models.users import User
from backend.models.messages import Message
from backend.models.meetings import Meeting

# Main entry point
if __name__ == "__main__":
    # Run the app on the port specified in the config
    app.run(debug=True, port=Config.PORT)
