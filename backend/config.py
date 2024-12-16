import os

from dotenv import load_dotenv
load_dotenv()


class Config:
    # Database configuration
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'JasonZoe@1985')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'parent_teacher_db')

    # Session configuration
    SESSION_SECRET = os.getenv('SESSION_SECRET', '45df67896lmg53244566bnmxz7s23ghds44dsa')

    # Port configuration
    PORT = int(os.getenv('PORT', 3500))

    # Frontend URL (for CORS)
    FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:5500')

    # Environment (development or production)
    NODE_ENV = os.getenv('NODE_ENV', 'development')
