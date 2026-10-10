from fastapi.testclient import TestClient
import pytest
from app import app


@pytest.fixture
def client():
    """Fixture that provides a TestClient instance for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def sample_payload():
    """Fixture that provides valid sample data for prediction testing."""
    return {
        "distance_km": 4.5,
        "prep_time_min": 15,
        "rider_available": 1,
        "is_raining": 1,
    }


def test_health_check(client):
    """Test the root health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "QuickBite ETA is live 🛵"}


def test_predict_endpoint(client, sample_payload):
    """Test the /predict endpoint with valid data using a fixture."""
    response = client.post("/predict", json=sample_payload)

    assert response.status_code == 200
    data = response.json()

    # Verify keys exist in the response
    assert "eta_minutes" in data
    assert "message" in data

    # Verify data types and formatting
    assert isinstance(data["eta_minutes"], float)
    assert f"Your food arrives in {data['eta_minutes']} min 🍔" == data["message"]


def test_predict_invalid_payload(client):
    """Test validation error when missing required fields."""
    invalid_payload = {
        "distance_km": 4.5
        # missing prep_time_min, rider_available, is_raining
    }
    response = client.post("/predict", json=invalid_payload)
    assert response.status_code == 422  # Unprocessable Entity