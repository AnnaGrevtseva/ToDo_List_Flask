def test_home_page_post(test_client):
    response = test_client.post('/')
    assert response.status_code == 404
    assert b"Todo App" not in response.data
