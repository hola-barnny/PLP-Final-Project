import sys
import urllib.parse
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Add /app to sys.path to fix import errors (optional if needed)
sys.path.append('/app')

# Import config and routes directly (no need for 'backend' prefix)
from config import Config
from routes.auth_routes import auth_bp
from routes.message_routes import message_bp
from routes.meeting_routes import meeting_bp
from models.users import User
from models.messages import Message
from models.meetings import Meeting

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

# Initialize the database and migration tools (no need to declare `db` twice)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register Blueprints for the routes
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(message_bp, url_prefix='/messages')
app.register_blueprint(meeting_bp, url_prefix='/meetings')

# Sample Route (ensure the app is running)
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

# Main entry point
if __name__ == "__main__":
    app.run(debug=True, port=Config.PORT)
