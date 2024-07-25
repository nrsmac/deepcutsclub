"""Methods for interacting with the Spotify API."""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from deepcuts_api.schemas import (
    Album,
    AlbumImageMetadata,
)
from deepcuts_api.settings import SpotifySettings

settings = SpotifySettings()


sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id=settings.client_id, client_secret=settings.client_secret)
)


def get_albums_by_artist(artist_name: str, limit: int = 20) -> list[Album]:
    """Get albums by artist name from Spotify."""
    results = sp.search(q=artist_name, limit=limit, type="artist")
    print(results.keys())
    artist_id = results["artists"]["items"][0]["id"]

    albums = []
    for album in sp.artist_albums(artist_id)["items"]:
        if album["name"] not in albums and album["album_type"] == "album":
            albums.append(
                Album(
                    name=album["name"],
                    artists=[artist["name"] for artist in album["artists"]],
                    release_date=album["release_date"],
                    total_tracks=album["total_tracks"],
                    tracks=[track["name"] for track in sp.album_tracks(album["id"])["items"]],
                    image=AlbumImageMetadata(
                        height=album["images"][0]["height"],
                        width=album["images"][0]["width"],
                        url=album["images"][0]["url"],
                    ),
                    spotify_url=album["external_urls"]["spotify"],
                )
            )
    return albums
