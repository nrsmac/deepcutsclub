"""Module to generate unique deepcuts identifiers."""

import string

from deepcuts_api.settings import SpotifySettings
from spotipy import (
    Spotify,
    SpotifyClientCredentials,
)


def get_isrc_from_spotify_track_link(spotify_link: str) -> str:
    """Extract the ISRC from a Spotify URI."""
    settings = SpotifySettings()
    client = Spotify(
        auth_manager=SpotifyClientCredentials(client_id=settings.client_id, client_secret=settings.client_secret)
    )

    spotify_uri = spotify_link.split("/")[-1]
    track = client.track(spotify_uri)
    return track["external_ids"]["isrc"]


def get_upc_from_spotify_album_link(spotify_link: str) -> str:
    """Extract the UPC from a Spotify Album URI."""
    settings = SpotifySettings()
    client = Spotify(
        auth_manager=SpotifyClientCredentials(client_id=settings.client_id, client_secret=settings.client_secret)
    )

    spotify_uri = spotify_link.split("/")[-1]
    album = client.album(spotify_uri)
    return album["external_ids"]["upc"]


def _base36_to_int(base36: str) -> int:
    """Convert a base36 string to an integer."""
    return int(base36, 36)


def _int_to_base62(num: int) -> str:
    """Convert an integer to a base62 string."""
    chars = string.digits + string.ascii_letters
    base62 = []
    while num:
        num, rem = divmod(num, 62)
        base62.append(chars[rem])
    return "".join(reversed(base62))


def _generate_unique_id(identifier: str) -> str:
    """Generate a short, unique, 7 character, alphanumeric identifier from an ISRC or UPC."""
    # Remove the country code from the ISRC
    identifier = identifier[2:]

    # Convert the identifier to a base 36 number
    base36_num = _base36_to_int(identifier)

    # Convert the base 36 number to a base 62 number
    base62_num = _int_to_base62(base36_num)

    return base62_num[:7]


def get_unique_id_from_spotify_link(spotify_link: str) -> str:
    """Extract the unique identifier from a Spotify URI."""
    if "track" in spotify_link:
        isrc = get_isrc_from_spotify_track_link(spotify_link)
        unique_id = _generate_unique_id(isrc)
    elif "album" in spotify_link:
        upc = get_upc_from_spotify_album_link(spotify_link)
        unique_id = _generate_unique_id(upc)
    else:
        raise ValueError("Can only extract ISRC from track or album Spotify URIs.")

    return unique_id
