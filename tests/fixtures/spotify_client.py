"""Fixtures for the Spotify client."""

from unittest.mock import patch

import pytest


@pytest.fixture
def mock_spotify_client():
    """Mock the Spotify client."""
    with patch("deepcuts_api.spotify.spotipy.Spotify") as mock_spotify:
        mock_instance = mock_spotify.return_value
        yield mock_instance
