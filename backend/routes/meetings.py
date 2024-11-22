from flask import Blueprint, request, jsonify
from models import Meeting, db

meetings = Blueprint('meetings', __name__)

@meetings.route('/schedule', methods=['POST'])
def schedule_meeting():
    data = request.json
    meeting = Meeting(teacher_id=data['teacher_id'], parent_id=data['parent_id'], date=data['date'], notes=data['notes'])
    db.session.add(meeting)
    db.session.commit()
    return jsonify({"message": "Meeting scheduled successfully!"}), 201

@meetings.route('/get/<int:user_id>', methods=['GET'])
def get_meetings(user_id):
    meetings = Meeting.query.filter((Meeting.teacher_id == user_id) | (Meeting.parent_id == user_id)).all()
    return jsonify([{"date": m.date, "notes": m.notes} for m in meetings])
