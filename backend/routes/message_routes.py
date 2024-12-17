from flask import Blueprint, request, jsonify
from app import db  # Import db directly from app.py
from models.messages import Message  # Import Message model

# Define the blueprint
message_bp = Blueprint('message', __name__)

@message_bp.route('/', methods=['GET'])
def get_messages():
    # Retrieve all messages
    messages = Message.query.all()
    return jsonify([{
        "id": m.id,
        "sender_id": m.sender_id,
        "receiver_id": m.receiver_id,
        "content": m.content,
        "timestamp": m.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp if needed
    } for m in messages])

@message_bp.route('/', methods=['POST'])
def send_message():
    # Create a new message from the request JSON data
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    content = data.get('content')
    
    # Create and save the new message
    new_message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Message sent successfully"}), 201
