from flask import Blueprint, request, jsonify
from models import Message, db
from firebase_utils import send_firebase_notification  # Import Firebase helper

messages = Blueprint('messages', __name__)

@messages.route('/send', methods=['POST'])
def send_message():
    data = request.json
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    content = data['content']

    # Create new message record
    new_message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(new_message)
    db.session.commit()

    # Send Firebase notification to the receiver
    send_firebase_notification(receiver_id, content)  # Notify receiver with message content

    return jsonify({"message": "Message sent!"}), 201

@messages.route('/get/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    messages = Message.query.filter((Message.sender_id == user_id) | (Message.receiver_id == user_id)).all()
    return jsonify([{"content": m.content, "timestamp": m.timestamp} for m in messages])
