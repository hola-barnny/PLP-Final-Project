import pytest
from app import app
from flask import json

# Setup for test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test case for user login endpoint
def test_login(client):
    response = client.post('/login', json={
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in response.json
    assert response.json['token'] != ''  # Ensure that token is non-empty

# Test case for invalid login attempt
def test_invalid_login(client):
    response = client.post('/login', json={
        'email': 'testuser@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid credentials'

# Test case for registering a new user
def test_register_user(client):
    response = client.post('/register', json={
        'email': 'newuser@example.com',
        'password': 'password123',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'User created successfully'

# Test case for sending a message
def test_send_message(client):
    response = client.post('/message', json={
        'sender_id': '1',
        'receiver_id': '2',
        'content': 'Hello, how are you?'
    })
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'Message sent successfully'

# Test case for fetching messages between users
def test_get_messages(client):
    response = client.get('/messages/1')  # Assume '1' is the user ID
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) >= 0  # At least an empty list if no messages

# Test case for creating a meeting
def test_create_meeting(client):
    response = client.post('/meeting', json={
        'teacher_id': '1',
        'parent_id': '2',
        'date_time': '2024-12-15T10:00:00',
        'agenda': 'Discuss student progress'
    })
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'Meeting created successfully'

# Test case for retrieving all meetings of a user
def test_get_meetings(client):
    response = client.get('/meetings/1')  # Assume '1' is the user ID
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) >= 0  # At least an empty list if no meetings

# Test case for updating user information
def test_update_user_info(client):
    response = client.put('/user/1', json={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'User information updated successfully'

# Test case for deleting a user
def test_delete_user(client):
    response = client.delete('/user/2')  # Assume '2' is the user ID to be deleted
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'User deleted successfully'

# Test case for retrieving user profile data
def test_get_user_profile(client):
    response = client.get('/user/1')  # Assume '1' is the user ID
    assert response.status_code == 200
    assert 'email' in response.json
    assert 'first_name' in response.json
    assert 'last_name' in response.json
