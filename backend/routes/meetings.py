from flask import Blueprint, request, jsonify
from models import Meeting, db
from firebase_utils import send_firebase_notification  # Import Firebase notification helper

meetings = Blueprint('meetings', __name__)

@meetings.route('/schedule', methods=['POST'])
def schedule_meeting():
    data = request.json
    meeting = Meeting(teacher_id=data['teacher_id'], parent_id=data['parent_id'], date=data['date'], notes=data['notes'])
    db.session.add(meeting)
    db.session.commit()
    
    # Send notifications to teacher and parent about the new meeting
    send_firebase_notification(data['teacher_id'], f"New meeting scheduled: {data['date']}")
    send_firebase_notification(data['parent_id'], f"New meeting scheduled: {data['date']}")
    
    return jsonify({"message": "Meeting scheduled successfully!"}), 201

@meetings.route('/get/<int:user_id>', methods=['GET'])
def get_meetings(user_id):
    meetings = Meeting.query.filter((Meeting.teacher_id == user_id) | (Meeting.parent_id == user_id)).all()
    return jsonify([{"date": m.date, "notes": m.notes} for m in meetings])
