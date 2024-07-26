"""Unit tests for deepcuts_api/spotify.py."""

from unittest.mock import patch

from deepcuts_api import spotify


def test_get_albums_by_artist_success(mock_spotify):
    """Test getting albums by artist successfully."""
    # Patch the spotipy.Spotify instance with the mock object
    with patch("deepcuts_api.spotify.sp", new=mock_spotify):
        albums = spotify.get_albums_by_artist("Mock Artist")

    assert len(albums) > 0
    assert albums[0].name == "Mock Album"
    assert albums[0].release_date == "2024-01-01"


def test_get_albums_by_artist_empty_results(mock_spotify):
    """Test getting albums by artist returns empty list when no results found."""
    # Modify the mock to return an empty result
    mock_spotify.search.return_value = {"artists": {"items": []}}

    with patch("deepcuts_api.spotify.sp", new=mock_spotify):
        albums = spotify.get_albums_by_artist("NonExistentArtist")

    assert len(albums) == 0
