import os
import pytest
from src import create_app


@pytest.fixture
def client():
    app = create_app(testing=True)
    yield app.test_client()

    os.remove("src/data/test.db")
