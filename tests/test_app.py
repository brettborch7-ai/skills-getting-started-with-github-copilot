from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_signup_rejects_duplicate_email():
    response = client.post("/activities/Chess Club/signup?email=michael@mergington.edu")

    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_unregister_participant_from_activity():
    activity_name = "Basketball Team"
    email = "newstudent@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    assert unregister_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]
