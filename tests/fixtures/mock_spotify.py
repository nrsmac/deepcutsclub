"""Fixture to mock Spotify API responses."""

from unittest.mock import Mock

import pytest


@pytest.fixture(scope="function")
def mock_spotify():
    """Fixture to mock Spotify API responses."""
    mock = Mock()
    mock.search.return_value = {"artists": {"items": [{"id": "mockArtistId", "name": "Mock Artist"}]}}
    mock.artist_albums.return_value = {
        "items": [
            {
                "id": "mockAlbumId",
                "name": "Mock Album",
                "album_type": "album",
                "release_date": "2024-01-01",
                "total_tracks": 10,
                "artists": [{"name": "Mock Artist"}],
                "images": [{"height": 640, "width": 480, "url": "https://example.com/image.jpg"}],
                "external_urls": {"spotify": "https://open.spotify.com/album/mockAlbumId"},
            }
        ]
    }
    mock.album_tracks.return_value = {
        "items": [{"name": "Track 1", "external_urls": {"spotify": "https://open.spotify.com/track/mockTrackId"}}]
    }
    return mock
