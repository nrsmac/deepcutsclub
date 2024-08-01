"""Unit tests for deepcuts_api/spotify.py."""

from unittest.mock import patch

import pytest

from deepcuts_api.genres import Genre
from deepcuts_api.schemas import (
    Album,
    Artist,
)
from deepcuts_api.spotify import get_recommendations


@pytest.fixture
def mock_spotify():
    """Mock the Spotify client."""
    with patch("deepcuts_api.spotify.spotipy.Spotify") as mock_spotify:
        yield mock_spotify


def test_get_recommendations_valid_input(mock_spotify):
    """Test getting recommendations with valid input."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"artists": {"items": [{"id": "artist_id_1"}]}},
        {"albums": {"items": [{"id": "album_id_1"}]}},
    ]
    mock_spotify_instance.recommendations.return_value = {
        "tracks": [
            {
                "album": {
                    "name": "Album 1",
                    "artists": [{"name": "Artist 1"}],
                    "id": "album_id_1",
                    "images": [{"url": "http://image.url/1"}],
                }
            }
        ]
    }

    artists = [Artist(name="Artist 1")]
    albums = [Album(title="Album 1", artist_name="Artist 1", spotify_id="album_id_1", image_url="http://image.url/1")]
    genres = [Genre.ROCK]

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 1
    assert recommendations[0].title == "Album 1"
    assert recommendations[0].artist_name == "Artist 1"
    assert recommendations[0].spotify_id == "album_id_1"
    assert recommendations[0].image_url == "http://image.url/1"


def test_get_recommendations_empty_input(mock_spotify):
    """Test getting recommendations with empty input."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.recommendations.return_value = {"tracks": []}

    artists = []
    albums = []
    genres = [Genre.ROCK]

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 0


def test_get_recommendations_none_genres(mock_spotify):
    """Test getting recommendations with None genres."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"artists": {"items": [{"id": "artist_id_1"}]}},
        {"albums": {"items": [{"id": "album_id_1"}]}},
    ]
    mock_spotify_instance.recommendations.return_value = {
        "tracks": [
            {
                "album": {
                    "name": "Album 1",
                    "artists": [{"name": "Artist 1"}],
                    "id": "album_id_1",
                    "images": [{"url": "http://image.url/1"}],
                }
            }
        ]
    }

    artists = [Artist(name="Artist 1")]
    albums = [Album(title="Album 1", artist_name="Artist 1", spotify_id="album_id_1", image_url="http://image.url/1")]
    genres = None

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 1
    assert recommendations[0].title == "Album 1"
    assert recommendations[0].artist_name == "Artist 1"
    assert recommendations[0].spotify_id == "album_id_1"
    assert recommendations[0].image_url == "http://image.url/1"


def test_get_recommendations_no_artists(mock_spotify):
    """Test getting recommendations with no artists."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"albums": {"items": [{"id": "album_id_1"}]}},
    ]
    mock_spotify_instance.recommendations.return_value = {
        "tracks": [
            {
                "album": {
                    "name": "Album 1",
                    "artists": [{"name": "Artist 1"}],
                    "id": "album_id_1",
                    "images": [{"url": "http://image.url/1"}],
                }
            }
        ]
    }

    artists = []
    albums = [Album(title="Album 1", artist_name="Artist 1", spotify_id="album_id_1", image_url="http://image.url/1")]
    genres = [Genre.ROCK]

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 1
    assert recommendations[0].title == "Album 1"
    assert recommendations[0].artist_name == "Artist 1"
    assert recommendations[0].spotify_id == "album_id_1"
    assert recommendations[0].image_url == "http://image.url/1"


def test_get_recommendations_no_albums(mock_spotify):
    """Test getting recommendations with no albums."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"artists": {"items": [{"id": "artist_id_1"}]}},
    ]
    mock_spotify_instance.recommendations.return_value = {
        "tracks": [
            {
                "album": {
                    "name": "Album 1",
                    "artists": [{"name": "Artist 1"}],
                    "id": "album_id_1",
                    "images": [{"url": "http://image.url/1"}],
                }
            }
        ]
    }

    artists = [Artist(name="Artist 1")]
    albums = []
    genres = [Genre.ROCK]

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 1
    assert recommendations[0].title == "Album 1"
    assert recommendations[0].artist_name == "Artist 1"
    assert recommendations[0].spotify_id == "album_id_1"
    assert recommendations[0].image_url == "http://image.url/1"


def test_get_recommendations_no_genres(mock_spotify):
    """Test getting recommendations with no genres."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"artists": {"items": [{"id": "artist_id_1"}]}},
        {"albums": {"items": [{"id": "album_id_1"}]}},
    ]
    mock_spotify_instance.recommendations.return_value = {
        "tracks": [
            {
                "album": {
                    "name": "Album 1",
                    "artists": [{"name": "Artist 1"}],
                    "id": "album_id_1",
                    "images": [{"url": "http://image.url/1"}],
                }
            }
        ]
    }

    artists = [Artist(name="Artist 1")]
    albums = [Album(title="Album 1", artist_name="Artist 1", spotify_id="album_id_1", image_url="http://image.url/1")]
    genres = []

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 1
    assert recommendations[0].title == "Album 1"
    assert recommendations[0].artist_name == "Artist 1"
    assert recommendations[0].spotify_id == "album_id_1"
    assert recommendations[0].image_url == "http://image.url/1"


def test_get_recommendations_invalid_artist(mock_spotify):
    """Test getting recommendations with invalid artist."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"artists": {"items": []}},
    ]
    mock_spotify_instance.recommendations.return_value = {"tracks": []}

    artists = [Artist(name="Invalid Artist")]
    albums = []
    genres = [Genre.ROCK]

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 0


def test_get_recommendations_invalid_album(mock_spotify):
    """Test getting recommendations with invalid album."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"albums": {"items": []}},
    ]
    mock_spotify_instance.recommendations.return_value = {"tracks": []}

    artists = []
    albums = [
        Album(
            title="Invalid Album",
            artist_name="Invalid Artist",
            spotify_id="invalid_id",
            image_url="http://invalid.url",
        )
    ]
    genres = [Genre.ROCK]

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 0


def test_get_recommendations_empty_spotify_response(mock_spotify):
    """Test getting recommendations with empty Spotify response."""
    mock_spotify_instance = mock_spotify.return_value
    mock_spotify_instance.search.side_effect = [
        {"artists": {"items": [{"id": "artist_id_1"}]}},
        {"albums": {"items": [{"id": "album_id_1"}]}},
    ]
    mock_spotify_instance.recommendations.return_value = {"tracks": []}

    artists = [Artist(name="Artist 1")]
    albums = [Album(title="Album 1", artist_name="Artist 1", spotify_id="album_id_1", image_url="http://image.url/1")]
    genres = [Genre.ROCK]

    recommendations = get_recommendations(artists, albums, genres)

    assert len(recommendations) == 0
