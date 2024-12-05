import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "classbridge_db")
    SESSION_SECRET = os.getenv("SESSION_SECRET", "default_secret")
    PORT = int(os.getenv("PORT", 3500))
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5500")
    NODE_ENV = os.getenv("NODE_ENV", "development")
