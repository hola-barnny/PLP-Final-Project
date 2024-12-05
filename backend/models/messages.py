# models/messages.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
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
        return f'<Message from {self.sender.full_name} to {self.receiver.full_name}>'

    def mark_as_read(self):
        self.read_at = datetime.utcnow()
