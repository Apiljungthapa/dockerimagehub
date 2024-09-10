import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client using the Flask app configured for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    # Send a GET request to the root URL
    response = client.get('/')
    
    # Check if the response data is "Hello, World!"
    assert response.data == b'Hello, World!'
    # Check if the status code is 200
    assert response.status_code == 200

def test_login_get(client):
    # Send a GET request to the /login URL
    response = client.get('/login')
    
    # Check if the response contains the login form
    assert b'<h2>Login</h2>' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data
    # Check if the status code is 200
    assert response.status_code == 200

def test_login_post(client):
    # Send a POST request to the /login URL with form data
    response = client.post('/login', data=dict(username='testuser', password='testpass'))
    
    # Check if the response contains the expected message
    assert b'Logged in as testuser' in response.data
    # Check if the status code is 200
    assert response.status_code == 200
