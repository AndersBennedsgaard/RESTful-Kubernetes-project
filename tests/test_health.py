from .fixtures import client


def test_index(client):
    assert client.get("/").get_data() == b"hello world", "App is not running correctly"


def test_health(client):
    assert client.get("/health").get_data() == b"healthy", "App is not running"
