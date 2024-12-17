from flask import Blueprint, request, jsonify
from backend import db  # Import SQLAlchemy instance
from backend.models.meetings import Meeting  # Import Meeting model

# Define the blueprint
meeting_bp = Blueprint('meeting', __name__)

@meeting_bp.route('/', methods=['GET'])
def get_meetings():
    # Retrieve all meetings
    meetings = Meeting.query.all()
    return jsonify([{
        "id": m.id,
        "title": m.title,
        "date": m.date,
        "time": m.time,
        "participants": m.participants
    } for m in meetings])

@meeting_bp.route('/', methods=['POST'])
def schedule_meeting():
    # Create a new meeting from the request JSON data
    data = request.json
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    participants = data.get('participants')
    
    # Create and save the new meeting
    new_meeting = Meeting(title=title, date=date, time=time, participants=participants)
    db.session.add(new_meeting)
    db.session.commit()
    
    return jsonify({"message": "Meeting scheduled successfully"}), 201
