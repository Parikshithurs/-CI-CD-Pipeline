import pytest
import sys
import os

# Make sure Python can find the app folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from main import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Tests ────────────────────────────────────────────────

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_add_two_numbers(client):
    response = client.get("/add/3/4")
    assert response.status_code == 200
    assert response.json["result"] == 7


def test_add_negative_numbers(client):
    response = client.get("/add/-2/5")
    assert response.status_code == 200
    assert response.json["result"] == 3


def test_reverse_string(client):
    response = client.get("/reverse/hello")
    assert response.status_code == 200
    assert response.json["result"] == "olleh"


def test_reverse_single_char(client):
    response = client.get("/reverse/a")
    assert response.status_code == 200
    assert response.json["result"] == "a"