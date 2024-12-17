from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from extensions import db  # Import db from extensions.py

# Define the User model
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('teacher', 'parent', 'student'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    phone_number = db.Column(db.String(15))

    # Relationships
    messages = db.relationship('Message', backref='user', lazy=True)
    meetings = db.relationship('Meeting', backref='user', lazy=True)

    def __init__(self, name, email, password, role):  # Updated 'full_name' to 'name'
        self.name = name  # Updated to 'name'
        self.email = email
        self.password_hash = self.set_password(password)
        self.role = role

    def set_password(self, password):
        """
        This method hashes the password before storing it.
        """
        return generate_password_hash(password)

    def check_password(self, password):
        """
        This method checks if the provided password matches the hashed password in the database.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.name}, Role: {self.role}>'
