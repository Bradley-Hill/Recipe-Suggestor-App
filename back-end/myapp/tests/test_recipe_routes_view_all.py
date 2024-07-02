import pytest
from flask import json
from myapp import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_view_all(client):
    response = client.get('/view_all')

    assert response.status_code == 200