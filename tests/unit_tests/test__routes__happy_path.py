"""Unit tests for the happy path scenarios of the API routes."""

from fastapi.testclient import TestClient

from deepcuts_api.schemas import (
    Album,
    AlbumImageMetadata,
)

mj_albums = [  # Per schemas.py
    Album(
        name="Thriller",
        artists=["Michael Jackson"],
        release_date="1982-11-30",
        total_tracks=9,
        tracks=["Wanna Be Startin' Somethin'", "Baby Be Mine"],
        image=AlbumImageMetadata(
            height=640,
            width=640,
            url="https://i.scdn.co/image/ab67616d0000b273a2f4d1f4f5c9d2b5f6f0e1f2",
        ),
        spotify_url="https://open.spotify.com/album/1C2h7mLntPSeVYciMRTF4a",
    ),
    Album(
        name="Bad",
        artists=["Michael Jackson"],
        release_date="1987-08-31",
        total_tracks=10,
        tracks=["Bad", "The Way You Make Me Feel"],
        image=AlbumImageMetadata(
            height=640,
            width=640,
            url="https://i.scdn.co/image/ab67616d0000b273a2f4d1f4f5c9d2b5f6f0e1f2",
        ),
        spotify_url="https://open.spotify.com/album/1C2h7mLntPSeVYciMRTF4a",
    ),
]


def test_get_albums_by_artist(client: TestClient, mock_spotify: None):
    """Test getting albums by artist name."""
    artist = "Michael Jackson"
    mock_spotify.get_albums_by_artist.return_value = mj_albums  # type: ignore

    response = client.get(f"/albums/{artist}")
    assert response.status_code == 200
