from fastapi.testclient import TestClient
from aidevplat.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'template': 'python-service', 'tests_passed': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'template': 'python-service'}).json()
    assert bad["passed"] is False
    assert "tests" in bad["failed"]
