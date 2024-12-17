from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Message Model
class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    read_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    sender = db.relationship('User', foreign_keys=[sender_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])

    def __init__(self, sender_id, receiver_id, content):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content

    def __repr__(self):
        return f'<Message from {self.sender.name} to {self.receiver.name}>'  # Updated to use 'name'

    def mark_as_read(self):
        self.read_at = datetime.utcnow()


# User Model
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
    messages_sent = db.relationship('Message', foreign_keys=[Message.sender_id], backref='sender', lazy=True)
    messages_received = db.relationship('Message', foreign_keys=[Message.receiver_id], backref='receiver', lazy=True)

    # Add meetings relationship
    meetings = db.relationship('Meeting', backref='user', lazy=True)

    def __init__(self, name, email, password, role):
        self.name = name  # Updated to 'name'
        self.email = email
        self.password_hash = self.set_password(password)
        self.role = role

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.name}, Role: {self.role}>'
