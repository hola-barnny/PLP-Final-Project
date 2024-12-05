from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

# Configure the app with database and session secret
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}"
app.config['SECRET_KEY'] = Config.SESSION_SECRET
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Sample Route
@app.route("/")
def index():
    return "Parent-Teacher Communication App is running!"

if __name__ == "__main__":
    app.run(port=Config.PORT)
