from flask import request, jsonify
from routes import message_bp
from models.messages import Message  # Import Message model
from backend import db  # Import SQLAlchemy instance

@message_bp.route('/', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([{"id": m.id, "sender_id": m.sender_id, "receiver_id": m.receiver_id, "content": m.content, "timestamp": m.timestamp} for m in messages])

@message_bp.route('/', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    content = data.get('content')
    
    new_message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Message sent successfully"}), 201
