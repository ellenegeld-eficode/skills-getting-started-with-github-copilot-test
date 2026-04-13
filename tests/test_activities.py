def test_get_activities_returns_dictionary(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0


def test_get_activities_has_expected_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    for details in activities.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
