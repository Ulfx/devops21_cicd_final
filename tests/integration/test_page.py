
def test_home_page_with_fixture(test_client):
    response = test_client.get('/')
    assert response.status_code is not 404
    assert response.status_code == 200
    assert b"Welcome to the shop" in response.data
    assert b"Register" in response.data
    assert b"Log In" in response.data


def test_home_page_post_with_fixture(test_client):

    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Flaskr" not in response.data

def test_page_exists(test_client):
    response = test_client.get("/")
    assert response.status_code is not None