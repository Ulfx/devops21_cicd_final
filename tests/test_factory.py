from flask import Flask
from shop_app import create_app


def test_config():
    assert not create_app().testing


#def test_hello(client):
#    response = client.get("/hello")
#    assert response.data == b"Hello, World!"