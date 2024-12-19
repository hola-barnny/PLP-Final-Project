from extensions import db  # Import db from extensions.py
from datetime import datetime


class Meeting(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    meeting_date = db.Column(db.DateTime, nullable=False)
    agenda = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', foreign_keys=[user_id], backref='user_meetings')
    teacher = db.relationship('User', foreign_keys=[teacher_id], backref='teacher_meetings')

    def __init__(self, user_id, teacher_id, meeting_date, agenda):
        self.user_id = user_id
        self.teacher_id = teacher_id
        self.meeting_date = meeting_date
        self.agenda = agenda

    def __repr__(self):
        return f'<Meeting with Teacher ID {self.teacher_id} on {self.meeting_date}>'

    def formatted_time(self):
        if self.meeting_date:
            return self.meeting_date.strftime("%Y-%m-%d %H:%M:%S")
        return "No Date Set"
