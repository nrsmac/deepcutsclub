from src.id import (
    get_isrc_from_spotify_track_link,
    get_unique_id_from_spotify_link,
    get_upc_from_spotify_album_link,
)
from tests.consts import (
    TEST_ALBUM_DEEPCUTS_ID,
    TEST_ALBUM_SPOTIFY_UPC,
    TEST_ALBUM_SPOTIFY_URL,
    TEST_SONG_DEEPCUTS_ID,
    TEST_SONG_ISRC,
    TEST_SONG_SPOTIFY_URL,
)


def test_get_isrc_from_spotify_song_url(mock_spotify_client):  # type: ignore
    """Test that the ISRC is extracted from a Spotify song URL."""
    isrc = get_isrc_from_spotify_track_link(TEST_SONG_SPOTIFY_URL)
    assert isrc == TEST_SONG_ISRC


def test_get_isrc_from_spotify_song_url(mock_spotify_client):  # type: ignore
    """Test that the UPC is extracted from a Spotify album URL."""
    upc = get_upc_from_spotify_album_link(TEST_ALBUM_SPOTIFY_URL)
    assert upc == TEST_ALBUM_SPOTIFY_UPC


def test_get_isrc_from_spotify_song_url(mock_spotify_client):  # type: ignore
    """Test that the unique ID is extracted from a Spotify song URL."""
    unique_id = get_unique_id_from_spotify_link(TEST_SONG_SPOTIFY_URL)
    assert unique_id == TEST_SONG_DEEPCUTS_ID


def test_get_isrc_from_spotify_song_url(mock_spotify_client):  # type: ignore
    """Test that the unique ID is extracted from a Spotify album URL."""
    unique_id = get_unique_id_from_spotify_link(TEST_ALBUM_SPOTIFY_URL)
    assert unique_id == TEST_ALBUM_DEEPCUTS_ID
