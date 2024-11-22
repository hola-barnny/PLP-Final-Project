from flask import Blueprint, request, jsonify
from models import Message, db

messages = Blueprint('messages', __name__)

@messages.route('/send', methods=['POST'])
def send_message():
    data = request.json
    new_message = Message(sender_id=data['sender_id'], receiver_id=data['receiver_id'], content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": "Message sent!"}), 201

@messages.route('/get/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    messages = Message.query.filter((Message.sender_id == user_id) | (Message.receiver_id == user_id)).all()
    return jsonify([{"content": m.content, "timestamp": m.timestamp} for m in messages])
