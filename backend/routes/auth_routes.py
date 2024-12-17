from flask import request, jsonify
from werkzeug.security import check_password_hash
from . import auth_bp
from backend.models.users import User
from backend import db  # Import SQLAlchemy instance

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Fetch user from the database
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful", "user": {"id": user.id, "name": user.name}})
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400
    
    # Create a new user
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201
