import os
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app(testing=True)
    yield app.test_client()

    os.remove("app/test.db")
