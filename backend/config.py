# config.py
import os

class Config:
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'a_random_secret_key')
    DEBUG = True

    # Database settings for MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://user:password@localhost/dbname')
