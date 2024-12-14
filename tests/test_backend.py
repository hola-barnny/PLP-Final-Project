import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.post('/login', json={
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in response.json

def test_invalid_login(client):
    response = client.post('/login', json={
        'email': 'testuser@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'error' in response.json

def test_send_message(client):
    response = client.post('/message', json={
        'sender_id': '1',
        'receiver_id': '2',
        'content': 'Hello!'
    })
    assert response.status_code == 200
    assert 'message' in response.json

def test_get_messages(client):
    response = client.get('/messages/1')
    assert response.status_code == 200
    assert isinstance(response.json, list)
