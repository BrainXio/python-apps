
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "john", "email": "john@example.com", "password": "secret"})
    assert response.status_code == 200
    assert response.json()["username"] == "john"
    assert "password" not in response.json()

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
