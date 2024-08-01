"""API client fixture for FastAPI tests."""

import pytest
from fastapi.testclient import TestClient

from deepcuts_api.main import create_app
from deepcuts_api.settings import Settings


@pytest.fixture
def client() -> TestClient:  # type: ignore # pylint: disable=unused-argument
    """Fixture for FastAPI test client."""
    settings: Settings = Settings()
    app = create_app(settings)
    with TestClient(app) as client:
        yield client
