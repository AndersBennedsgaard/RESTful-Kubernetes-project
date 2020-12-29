from .fixtures import client


def test_health(client):
    assert client.get("/health").json == "healthy", "App is not running"
