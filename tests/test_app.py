from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "broken"}


def test_home_reports_version_and_never_leaks_secret():
    body = client.get("/").json()
    assert body["version"]
    assert isinstance(body["secretConfigured"], bool)
    assert "DEMO_SECRET" not in body
