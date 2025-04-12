import sys
import os
import pytest

# Add the project root to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, CircleCI!"}
