import pytest
from flask_testing import TestClient
from wgsi import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
