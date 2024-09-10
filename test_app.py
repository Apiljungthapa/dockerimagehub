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
