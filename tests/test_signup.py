def test_signup_successfully_adds_participant(client):
    response = client.post("/activities/Programming%20Class/signup?email=newstudent@mergington.edu")

    assert response.status_code == 200
    assert response.json()["message"] == "Signed up newstudent@mergington.edu for Programming Class"

    activities = client.get("/activities").json()
    assert "newstudent@mergington.edu" in activities["Programming Class"]["participants"]


def test_signup_returns_404_for_unknown_activity(client):
    response = client.post("/activities/Unknown%20Club/signup?email=student@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_participant(client):
    response = client.post("/activities/Chess%20Club/signup?email=michael@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_requires_email_query_parameter(client):
    response = client.post("/activities/Chess%20Club/signup")

    assert response.status_code == 422
