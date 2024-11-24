from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db

auth = Blueprint('auth', __name__)

# Register route
@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'])

    # Add fcm_token to the registration data
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        role=data['role'],
        fcm_token=data.get('fcm_token')  # Storing FCM token on registration
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

# Login route
@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and check_password_hash(user.password, data['password']):
        fcm_token = data.get('fcm_token')
        if fcm_token:
            user.fcm_token = fcm_token
            db.session.commit()

        return jsonify({"message": "Login successful!", "user_id": user.id})

    return jsonify({"error": "Invalid credentials"}), 401

# New route to update FCM tokens for multiple users
@auth.route('/update_tokens', methods=['POST'])
def update_fcm_tokens():
    data = request.json  # Expecting a list of user_id and fcm_token pairs
    try:
        # Loop through the provided data
        for user_data in data:
            user_id = user_data['user_id']
            new_fcm_token = user_data['fcm_token']

            # Fetch the user from the database
            user = User.query.filter_by(id=user_id).first()

            # If the user exists, update the fcm_token
            if user:
                user.fcm_token = new_fcm_token  # Set the new token
                db.session.commit()  # Commit the changes to the database
            else:
                return jsonify({"error": f"User with ID {user_id} not found"}), 404

        return jsonify({"message": "FCM tokens updated successfully!"}), 200
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500
