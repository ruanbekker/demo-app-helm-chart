import pytest
from src.main import app, db
from src.api.models import Item

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_get_items(client):
    response = client.get("/api/items")
    assert response.status_code == 200
    assert response.json == []

def test_add_item(client):
    response = client.post("/api/items", json={"name": "Test Item", "description": "Test Description"})
    assert response.status_code == 201
    assert response.json["message"] == "Item added successfully!"

