import pytest
import os
from shop_app import create_app


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


CONNECTION_TIMEOUT = 1
READ_TIMEOUT = 5


class Config:
    def __init__(self):
        target_host = os.getenv("TARGET_HOST", "127.0.0.1")
        target_port = os.getenv("TARGET_PORT", 5000)
        self.base_url = f'http://{target_host}:{target_port}/'
        self.TIMEOUT = (CONNECTION_TIMEOUT, READ_TIMEOUT)


@pytest.fixture
def config():
    return Config()
