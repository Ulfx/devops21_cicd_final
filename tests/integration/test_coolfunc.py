def test_cool_resverseadv(test_client):
    response = test_client.get('/cool/reversedadv')
    assert response.status_code != 404
    assert response.status_code == 200
    assert b"This is a very cool text: dlroW olleH!" in response.data


def test_cool_reversed(test_client):
    response = test_client.get('/cool/reversed')
    assert response.status_code != 404
    assert response.status_code == 200
    assert b"dlroW olleH" in response.data
