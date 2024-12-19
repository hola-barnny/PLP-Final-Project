import sys
import urllib.parse
from flask import Flask, jsonify, render_template
from flask_migrate import Migrate
from flask_cors import CORS

# Add /app to sys.path to fix import errors (optional if needed)
sys.path.append('/app')

# Import config and routes directly (no need for 'backend' prefix)
from config import Config
from routes.auth_routes import auth_bp
from routes.message_routes import message_bp
from routes.meeting_routes import meeting_bp
from extensions import db  # Import db from extensions.py

# Initialize the app with explicit template and static folder paths
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.config.from_object(Config)

# URL encode the password if it contains special characters like '@'
DB_PASSWORD = urllib.parse.quote_plus(Config.DB_PASSWORD)

# Configure the app with database and session secret
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{Config.DB_USER}:{DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"
app.config['SECRET_KEY'] = Config.SESSION_SECRET
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize CORS for handling cross-origin requests
CORS(app)

# Initialize the database and migration tools (db now imported from extensions)
migrate = Migrate(app, db)

# Register Blueprints for the routes
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(message_bp, url_prefix='/messages')
app.register_blueprint(meeting_bp, url_prefix='/meetings')

# HTML Routes to render templates
@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/messaging")
def messaging():
    return render_template("messaging.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

# API health check route
@app.route("/api/health")
def api_health():
    return jsonify({"message": "Parent-Teacher Communication App is running!"})

# Error handling routes
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404  # Render a custom 404 page if available

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500  # Render a custom 500 page if available

# Main entry point
if __name__ == "__main__":
    app.run(debug=True, port=Config.PORT)
