# models/meetings.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Meeting(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    meeting_date = db.Column(db.DateTime, nullable=False)
    agenda = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', foreign_keys=[user_id])
    teacher = db.relationship('User', foreign_keys=[teacher_id])

    def __init__(self, user_id, teacher_id, meeting_date, agenda):
        self.user_id = user_id
        self.teacher_id = teacher_id
        self.meeting_date = meeting_date
        self.agenda = agenda

    def __repr__(self):
        return f'<Meeting with {self.teacher.full_name} on {self.meeting_date}>'

    def get_time(self):
        return self.meeting_date.strftime("%Y-%m-%d %H:%M:%S")

