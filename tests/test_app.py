from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "unregister-test@example.com"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_unregister_participant_raises_error_if_not_signed_up():
    activity_name = "Chess Club"
    email = "not-signed-up@example.com"

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert response.status_code == 400
