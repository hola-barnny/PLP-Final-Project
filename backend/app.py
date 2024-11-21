from flask import Flask, request, jsonify
import bcrypt
import mysql.connector
from mysql.connector import Error
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Flask app
app = Flask(__name__)

# Path to the Firebase Admin SDK credentials JSON file
cred = credentials.Certificate("firebase-adminsdk.json")

# Initialize the Firebase Admin SDK
firebase_admin.initialize_app(cred)

# MySQL database connection details
DB_HOST = 'localhost'
DB_USER = 'root'  # Your MySQL username
DB_PASSWORD = 'JasonZoe@1985'  # Your MySQL password
DB_NAME = 'parent_teacher_db'  # Your MySQL database name

# Utility function to connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
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

# Registration Route (User registration with MySQL)
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password'].encode('utf-8')

    # Hash password
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    try:
        # Connect to MySQL
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, hashed))
        conn.commit()
        return jsonify({"status": "User registered successfully"}), 201
    except Error as e:
        return jsonify({"status": f"Error: {str(e)}"}), 500
    finally:
        cursor.close()
        conn.close()

# Login Route (User login with MySQL)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password'].encode('utf-8')

    try:
        # Connect to MySQL
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, password FROM users WHERE email = %s", (email,))
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

# Send Push Notification Route (Firebase Cloud Messaging)
@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    token = data['token']  # Firebase device token for the user
    title = data['title']  # Notification title
    body = data['body']  # Notification body

    # Prepare the message to be sent
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token  # Target user using their Firebase device token
    )

    try:
        # Send the message using Firebase Cloud Messaging
        response = messaging.send(message)
        return jsonify({"status": "Notification sent", "response": response}), 200
    except Exception as e:
        return jsonify({"status": f"Error sending notification: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
