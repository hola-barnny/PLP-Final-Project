import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin SDK
cred = credentials.Certificate('firebase-adminsdk.json')
firebase_admin.initialize_app(cred)

from flask import Flask, request, jsonify
import bcrypt
import mysql.connector
from mysql.connector import Error
from config import DATABASE_CONFIG
import datetime
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
    name = data['name']
    email = data['email']
    password = data['password'].encode('utf-8')
    role = data['role']
    phone_number = data.get('phone_number')

    # Hash password
    hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        created_at = datetime.datetime.now()  # Current timestamp
        cursor.execute(
            "INSERT INTO Users (name, email, password_hash, role, created_at, phone_number) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, email, hashed, role, created_at, phone_number)
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
    progress = data.get('progress', 'not started')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Students (name, grade, parent_id, progress) VALUES (%s, %s, %s, %s)",
            (name, grade, parent_id, progress)
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
    agenda = data.get('agenda', '')

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
        
@app.route('/api/meetings/<int:user_id>', methods=['GET'])
def get_meetings(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Fetch meetings for the user as either teacher or parent
    cursor.execute('''
        SELECT * FROM Meetings 
        WHERE teacher_id = %s OR parent_id = %s
    ''', (user_id, user_id))
    meetings = cursor.fetchall()
    conn.close()
    
    if meetings:
        return jsonify([{
            "id": meeting[0],
            "teacher_id": meeting[1],
            "parent_id": meeting[2],
            "date": meeting[3],
            "time": meeting[4],
            "status": meeting[5],
            "agenda": meeting[6]
        } for meeting in meetings])
    else:
        return jsonify({"message": "No meetings found for this user."}), 404


### MESSAGE ROUTES ###

# Send a Message
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    message = data['message']
    timestamp = datetime.datetime.now()
    status = data['status']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Messages (sender_id, receiver_id, message, timestamp, status) VALUES (%s, %s, %s,  %s, %s)",
            (sender_id, receiver_id, message, timestamp, status)
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
    timestamp = datetime.datetime.now()  # Current timestamp
    is_read = False

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Notifications (user_id, notification_type, message, status, timestamp, is_read) VALUES (%s, %s, %s, %s)",
            (user_id, notification_type, message, 'sent', timestamp, is_read)
        )
        conn.commit()
        return jsonify({"status": "Notification sent successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()
        
@app.route('/api/notifications/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Notifications WHERE user_id = %s', (user_id,))
    notifications = cursor.fetchall()
    conn.close()
    
    if notifications:
        return jsonify([{
            "id": notif[0],
            "user_id": notif[1],
            "notification_type": notif[2],
            "message": notif[3],
            "status": notif[4],
            "timestamp": notif[5],
            "is_read": notif[6]
        } for notif in notifications])
    else:
        return jsonify({"message": "No notifications found for this user."}), 404


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
