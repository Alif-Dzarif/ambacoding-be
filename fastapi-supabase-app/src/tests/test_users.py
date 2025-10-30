from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User
from app.crud.user import create_user
from app.schemas.user import UserCreate
import pytest

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def create_test_user():
    user_data = UserCreate(email="testuser@example.com", password="password")
    user = create_user(user_data)
    return user

def test_create_user(client):
    response = client.post("/api/v1/users/", json={"email": "newuser@example.com", "password": "password"})
    assert response.status_code == 201
    assert response.json()["email"] == "newuser@example.com"

def test_get_user(client, create_test_user):
    response = client.get(f"/api/v1/users/{create_test_user.id}")
    assert response.status_code == 200
    assert response.json()["email"] == create_test_user.email

def test_update_user(client, create_test_user):
    response = client.put(f"/api/v1/users/{create_test_user.id}", json={"email": "updateduser@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "updateduser@example.com"

def test_delete_user(client, create_test_user):
    response = client.delete(f"/api/v1/users/{create_test_user.id}")
    assert response.status_code == 204

    response = client.get(f"/api/v1/users/{create_test_user.id}")
    assert response.status_code == 404