from flask import Flask, request, jsonify
import bcrypt
import mysql.connector

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password'].encode('utf-8')

    # Hash password
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    # Connect to MySQL database (make sure MySQL is running)
    conn = mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="your_database"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                   (username, email, hashed))
    conn.commit()

    return jsonify({"status": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password'].encode('utf-8')

    # Check credentials
    conn = mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="your_database"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password, result[0].encode('utf-8')):
        return jsonify({"status": "Login successful"}), 200
    else:
        return jsonify({"status": "Invalid credentials"}), 400

if __name__ == '__main__':
    app.run(debug=True)
