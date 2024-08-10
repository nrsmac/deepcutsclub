"""Unit tests for the ID module."""

import pytest

from deepcuts_api.deepcuts_id import (
    get_isrc_from_apple_music_track_link,
    get_isrc_from_spotify_track_link,
    get_unique_id_from_apple_music_link,
    get_unique_id_from_spotify_link,
    get_upc_from_apple_music_album_link,
    get_upc_from_spotify_album_link,
)
from tests.consts import (
    TEST_ALBUM_APPLE_MUSIC_URL,
    TEST_ALBUM_DEEPCUTS_ID,
    TEST_ALBUM_SPOTIFY_URL,
    TEST_ALBUM_UPC,
    TEST_SONG_APPLE_MUSIC_URL,
    TEST_SONG_DEEPCUTS_ID,
    TEST_SONG_ISRC,
    TEST_SONG_SPOTIFY_URL,
)


def test_get_isrc_from_spotify_song_url(mock_spotify_client):  # pylint: disable=unused-argument
    """Test that the ISRC is extracted from a Spotify song URL."""
    isrc = get_isrc_from_spotify_track_link(TEST_SONG_SPOTIFY_URL)
    assert isrc == TEST_SONG_ISRC


def test_get_upc_from_spotify_album_url(mock_spotify_client):  # pylint: disable=unused-argument
    """Test that the UPC is extracted from a Spotify album URL."""
    upc = get_upc_from_spotify_album_link(TEST_ALBUM_SPOTIFY_URL)
    assert upc == TEST_ALBUM_UPC


def test_get_unique_id_from_spotify_song_url(mock_spotify_client):  # pylint: disable=unused-argument
    """Test that the unique ID is extracted from a Spotify song URL."""
    unique_id = get_unique_id_from_spotify_link(TEST_SONG_SPOTIFY_URL)
    assert unique_id == TEST_SONG_DEEPCUTS_ID


@pytest.mark.skip(reason="Apple Music is not yet implemented.")
def test_get_isrc_from_apple_music_song_url():
    """Test that the ISRC is extracted from an Apple Music song URL."""
    isrc = get_isrc_from_apple_music_track_link(TEST_SONG_APPLE_MUSIC_URL)
    assert isrc == TEST_SONG_ISRC


@pytest.mark.skip(reason="Apple Music is not yet implemented.")
def test_get_upc_from_apple_music_album_url():
    """Test that the UPC is extracted from an Apple Music album URL."""
    upc = get_upc_from_apple_music_album_link(TEST_ALBUM_APPLE_MUSIC_URL)  # pylint: disable=assignment-from-no-return
    assert upc == TEST_ALBUM_UPC


@pytest.mark.skip(reason="Apple Music is not yet implemented.")
def test_get_unique_id_from_apple_music_song_url():
    """Test that the unique ID is extracted from an Apple Music song URL."""
    unique_id = get_unique_id_from_apple_music_link(TEST_SONG_APPLE_MUSIC_URL)
    assert unique_id == TEST_SONG_DEEPCUTS_ID


@pytest.mark.skip(reason="Apple Music is not yet implemented.")
def test_get_unique_id_from_apple_music_album_url():
    """Test that the unique ID is extracted from an Apple Music album URL."""
    unique_id = get_unique_id_from_apple_music_link(TEST_ALBUM_APPLE_MUSIC_URL)
    assert unique_id == TEST_ALBUM_DEEPCUTS_ID


@pytest.mark.skip(reason="Apple Music is not yet implemented.")
def test_song_from_apple_music_and_spotify_have_same_unique_id():
    """Test that the unique ID is the same for a song on Apple Music and Spotify."""
    spotify_unique_id = get_unique_id_from_spotify_link(TEST_SONG_SPOTIFY_URL)
    apple_music_unique_id = get_unique_id_from_apple_music_link(TEST_SONG_APPLE_MUSIC_URL)
    assert spotify_unique_id == apple_music_unique_id
