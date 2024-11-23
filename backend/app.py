from flask import Flask, request, jsonify
import bcrypt
import mysql.connector
from mysql.connector import Error
from config import DATABASE_CONFIG
from firebase_config import *  # Firebase initialization
from firebase_admin import messaging

# Initialize Flask app
app = Flask(__name__)

# MySQL database connection details
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'JasonZoe@1985'
DB_NAME = 'parent_teacher_db'

# Utility function to connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host=DATABASE_CONFIG['host'],
        user=DATABASE_CONFIG['user'],
        password=DATABASE_CONFIG['password'],
        database=DATABASE_CONFIG['database']
    )
    return conn

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Parent-Teacher Communication App"})

# Handle favicon request (optional)
@app.route('/favicon.ico')
def favicon():
    return '', 204

### USER ROUTES ###

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password'].encode('utf-8')
    role = data['role']

    # Hash password
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (username, email, password_hash, role) VALUES (%s, %s, %s, %s)",
            (username, email, hashed, role)
        )
        conn.commit()
        return jsonify({"status": "User registered successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password').encode('utf-8')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, password_hash FROM Users WHERE email = %s", (email,))
        result = cursor.fetchone()

        if result and bcrypt.checkpw(password, result[1].encode('utf-8')):
            return jsonify({"status": "Login successful", "user_id": result[0]}), 200
        else:
            return jsonify({"status": "Invalid credentials"}), 400
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

### STUDENT ROUTES ###

# Add a Student
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data['name']
    grade = data['grade']
    parent_id = data['parent_id']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Students (name, grade, parent_id) VALUES (%s, %s, %s)",
            (name, grade, parent_id)
        )
        conn.commit()
        return jsonify({"status": "Student added successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

### MEETING ROUTES ###

# Schedule a Meeting
@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
    data = request.get_json()
    teacher_id = data['teacher_id']
    parent_id = data['parent_id']
    date = data['date']
    time = data['time']
    agenda = data['agenda']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Meetings (teacher_id, parent_id, date, time, agenda, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (teacher_id, parent_id, date, time, agenda, 'scheduled')
        )
        conn.commit()
        return jsonify({"status": "Meeting scheduled successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

### MESSAGE ROUTES ###

# Send a Message
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    content = data['content']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Messages (sender_id, receiver_id, message) VALUES (%s, %s, %s)",
            (sender_id, receiver_id, content)
        )
        conn.commit()
        return jsonify({"status": "Message sent successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

### NOTIFICATION ROUTES ###

# Send a Notification
@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    user_id = data['user_id']
    notification_type = data['notification_type']
    message = data['message']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Notifications (user_id, notification_type, message, status) VALUES (%s, %s, %s, %s)",
            (user_id, notification_type, message, 'sent')
        )
        conn.commit()
        return jsonify({"status": "Notification sent successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

### STUDENT PROGRESS ROUTES ###

# Get Student Progress
@app.route('/student_progress/<int:student_id>', methods=['GET'])
def get_student_progress(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Student_Progress WHERE student_id = %s", (student_id,))
        progress = cursor.fetchone()
        if progress:
            return jsonify(progress), 200
        else:
            return jsonify({"message": "Student progress not found"}), 404
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
