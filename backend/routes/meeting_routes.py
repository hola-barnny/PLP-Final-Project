from flask import Blueprint, request, jsonify
from app import db  # Import SQLAlchemy instance from app.py
from models.meetings import Meeting  # Import Meeting model

# Define the blueprint
meeting_bp = Blueprint('meeting', __name__)

@meeting_bp.route('/', methods=['GET'])
def get_meetings():
    # Retrieve all meetings
    meetings = Meeting.query.all()
    return jsonify([{
        "id": m.id,
        "user_id": m.user_id,
        "teacher_id": m.teacher_id,
        "meeting_date": m.formatted_time(),
        "agenda": m.agenda
    } for m in meetings])

@meeting_bp.route('/', methods=['POST'])
def schedule_meeting():
    # Create a new meeting from the request JSON data
    data = request.json
    user_id = data.get('user_id')
    teacher_id = data.get('teacher_id')
    meeting_date = data.get('meeting_date')
    agenda = data.get('agenda')
    
    # Create and save the new meeting
    new_meeting = Meeting(user_id=user_id, teacher_id=teacher_id, meeting_date=meeting_date, agenda=agenda)
    db.session.add(new_meeting)
    db.session.commit()
    
    return jsonify({"message": "Meeting scheduled successfully"}), 201
