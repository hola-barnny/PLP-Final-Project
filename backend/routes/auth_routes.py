from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from . import auth_bp
from models.users import User
from extensions import db  # Import db from extensions.py

# Route to log in a user and generate a JWT token
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Fetch user from the database
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        # Create a JWT token
        access_token = create_access_token(identity=user.id)
        return jsonify({"message": "Login successful", "access_token": access_token, "user": {"id": user.id, "name": user.name}})
    
    return jsonify({"error": "Invalid credentials"}), 401

# Route to sign up a new user
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400
    
    # Hash the password before saving it to the database
    hashed_password = generate_password_hash(password)
    
    # Create a new user
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201
