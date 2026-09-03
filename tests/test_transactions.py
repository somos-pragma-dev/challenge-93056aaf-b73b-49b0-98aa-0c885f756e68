from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from..src.main.app.database.database import get_db
from..src.main.app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_transaction():
    response = client.post(
        "/transactions/",
        json={"user_id": 1, "amount": 100.0, "description": "Test transaction"},
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "user_id": 1, "amount": 100.0, "description": "Test transaction"}

def test_read_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "user_id": 1, "amount": 100.0, "description": "Test transaction"}]

def test_update_transaction():
    response = client.put(
        "/transactions/1",
        json={"amount": 200.0, "description": "Updated transaction"},
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "user_id": 1, "amount": 200.0, "description": "Updated transaction"}

def test_delete_transaction():
    response = client.delete("/transactions/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "user_id": 1, "amount": 200.0, "description": "Updated transaction"}