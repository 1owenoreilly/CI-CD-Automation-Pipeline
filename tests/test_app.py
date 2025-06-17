from app import app
import pytest


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home endpoint returns a welcome message."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to my CI/CD demo API!"}


def test_add_numbers(client):
    """Test the add endpoint with valid inputs."""
    response = client.get('/add?a=2&b=3')
    assert response.status_code == 200
    assert response.json == {"result": 6.0}


def test_multiply():
    client = app.test_client()
    response = client.get('/multiply/3.0/4.0')
    assert response.status_code == 200
    assert response.json['result'] == 12.0


def test_add_invalid_input(client):
    """Test the add endpoint with invalid inputs."""
    response = client.get('/add?a=invalid&b=3')
    assert response.status_code == 400
    assert "error" in response.json
