"""Fixtures for the Spotify client."""

import pytest
from unittest.mock import patch

@pytest.fixture
def mock_spotify_client():
    """Mock the Spotify client."""
    with patch("deepcuts_api.spotify.spotipy.Spotify") as MockSpotify:
        mock_instance = MockSpotify.return_value
        yield mock_instance
