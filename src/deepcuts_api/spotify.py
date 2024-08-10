"""Methods for interacting with the Spotify API."""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from deepcuts_api.genres import Genre
from deepcuts_api.schemas import (
    Album,
    Artist,
)
from deepcuts_api.settings import SpotifySettings

settings = SpotifySettings()


sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id=settings.client_id, client_secret=settings.client_secret)
)


def get_albums_by_artist(artist_name: str, limit: int = 20) -> list[Album]:
    """
    Retrieve a list of albums by the specified artist.

    Args
    ----
    artist_name (str):
        The name of the artist.
    limit (int, optional):
        The maximum number of albums to retrieve. Defaults to 20.

    Returns
    -------
    list[Album]:
        A list of Album objects representing the albums by the artist.

    """
    results = sp.search(q=artist_name, limit=limit, type="artist")
    items = results["artists"]["items"]
    if len(items) < 1:
        return []

    artist_id = items[0]["id"]

    albums = []
    for album in sp.artist_albums(artist_id)["items"]:
        if album["name"] not in albums and album["album_type"] == "album":
            albums.append(
                Album(
                    title=album["name"],
                    artist_name=album["artists"][0]["name"],
                    spotify_id=album["id"],
                    image_url=album["images"][0]["url"],
                )
            )
    return albums


def get_recommendations(artists: list[Artist], albums: list[Album], genres: list[Genre] | None) -> list[Album]:
    """
    Generate album recommendations based on artists and albums.

    This function takes a list of artists and albums as input and generates album recommendations based on them.
    It uses the Spotify API to search for the seed artist and album IDs, and then uses these IDs along with the
    specified genres to retrieve recommendations from Spotify.

    Args
    ----
        artists (list[Artist]): A list of Artist objects.
        albums (list[Album]): A list of Album objects.
        genres (list[Genre] | None): A list of Genre objects or None.

    Returns
    -------
        list[Album]: A list of recommended Album objects.

    """
    client = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(client_id=settings.client_id, client_secret=settings.client_secret)
    )

    # Ensure that genre is a valid instance of Genre

    seed_artist_ids = []
    for artist in artists:
        search_result = client.search(q=artist.name, type="artist")
        if "artists" in search_result and search_result["artists"]["items"]:
            seed_artist_ids.append(search_result["artists"]["items"][0]["id"])
        else:
            print(f"No artist found for {artist.name}")

    seed_album_ids = []
    for album in albums:
        search_result = client.search(q=album.title, type="album")
        if "albums" in search_result and search_result["albums"]["items"]:
            seed_album_ids.append(search_result["albums"]["items"][0]["id"])
        else:
            # Handle the case where no album is found
            print(f"No album found for {album.title}")

    recommendations = client.recommendations(seed_artists=seed_artist_ids, seed_albums=seed_album_ids, genres=genres)
    recommended_albums = []
    for recommendation in recommendations["tracks"]:
        recommended_albums.append(
            Album(
                title=recommendation["album"]["name"],
                artist_name=recommendation["album"]["artists"][0]["name"],
                spotify_id=recommendation["album"]["id"],
                spotify_url=recommendation["album"]["external_urls"]["spotify"],
                image_url=recommendation["album"]["images"][0]["url"],
            )
        )
    return recommended_albums
