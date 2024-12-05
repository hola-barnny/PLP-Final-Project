from flask import request, jsonify
from routes import meeting_bp
from models.meetings import Meeting, Meetingl
from backend import db

@meeting_bp.route('/', methods=['GET'])
def get_meetings():
    meetings = Meeting.query.all()
    return jsonify([{"id": m.id, "title": m.title, "date": m.date, "time": m.time, "participants": m.participants} for m in meetings])

@meeting_bp.route('/', methods=['POST'])
def schedule_meeting():
    data = request.json
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    participants = data.get('participants')
    
    new_meeting = Meeting(title=title, date=date, time=time, participants=participants)
    db.session.add(new_meeting)
    db.session.commit()
    return jsonify({"message": "Meeting scheduled successfully"}), 201
