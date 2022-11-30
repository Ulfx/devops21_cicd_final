def test_cool_reversed_page(test_client):
    response = test_client.get('/cool/reversed')
    assert response.status_code != 404
    assert response.status_code == 200
    assert b"This is a very cool text: dlroW olleH!" in response.data
    assert "Hello world"[::-1] == "dlrow olleH"
