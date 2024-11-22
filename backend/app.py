from flask import Flask, request, jsonify
import bcrypt
import mysql.connector
from mysql.connector import Error
from config import DATABASE_CONFIG
from firebase_config import *  # This imports Firebase initialization
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

# Handle the root URL (optional)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Parent-Teacher Communication APP"})

# Handle the favicon request (optional)
@app.route('/favicon.ico')
def favicon():
    return '', 204

# User Registration Route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password'].encode('utf-8')
    role = data['role']  # Added role for parent/teacher differentiation

    # Hash password
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    try:
        # Connect to MySQL
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (username, email, password, role) VALUES (%s, %s, %s, %s)",
            (username, email, hashed, role)
        )
        conn.commit()
        return jsonify({"status": "User registered successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

# User Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password').encode('utf-8')

    try:
        # Connect to MySQL
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, password FROM Users WHERE email = %s", (email,))
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

# Add a Student Route
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

# Send a Message Route
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
            "INSERT INTO Messages (sender_id, receiver_id, content) VALUES (%s, %s, %s)",
            (sender_id, receiver_id, content)
        )
        conn.commit()
        return jsonify({"status": "Message sent successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

# Schedule a Meeting Route
@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
    data = request.get_json()
    teacher_id = data['teacher_id']
    parent_id = data['parent_id']
    date = data['date']
    time = data['time']

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Meetings (teacher_id, parent_id, date, time) VALUES (%s, %s, %s, %s)",
            (teacher_id, parent_id, date, time)
        )
        conn.commit()
        return jsonify({"status": "Meeting scheduled successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

# Fetch Messages Route
@app.route('/messages/<int:user_id>', methods=['GET'])
def fetch_messages(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM Messages WHERE receiver_id = %s OR sender_id = %s",
            (user_id, user_id)
        )
        messages = cursor.fetchall()
        return jsonify(messages), 200
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

# Send Push Notification Route
@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    token = data['token']
    title = data['title']
    body = data['body']

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token
    )

    try:
        response = messaging.send(message)
        return jsonify({"status": "Notification sent", "response": response}), 200
    except Exception as e:
        return jsonify({"status": f"Error sending notification: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
