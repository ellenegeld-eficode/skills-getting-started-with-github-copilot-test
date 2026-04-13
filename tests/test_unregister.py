def test_unregister_successfully_removes_participant(client):
    response = client.delete("/activities/Chess%20Club/signup?email=michael@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"

    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete("/activities/Unknown%20Club/signup?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_if_student_not_signed_up(client):
    response = client.delete("/activities/Chess%20Club/signup?email=notfound@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_fails_when_repeated(client):
    first = client.delete("/activities/Chess%20Club/signup?email=michael@mergington.edu")
    second = client.delete("/activities/Chess%20Club/signup?email=michael@mergington.edu")

    assert first.status_code == 200
    assert second.status_code == 404
