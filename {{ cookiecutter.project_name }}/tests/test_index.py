def test_index_get(test_client):
    """Sample test, by default no routes are generated
    and should return a 404."""
    rv = test_client.get('/')
    assert rv.status_code == 404
