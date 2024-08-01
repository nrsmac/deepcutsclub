"""Discogs API module."""

import pickle
import time

import discogs_client
from loguru import logger as log

from deepcuts_api.schemas import (
    Album,
    Artist,
)
from deepcuts_api.settings import DiscogsSettings

DISCOGS_REQUEST_TOKEN_URL = "https://api.discogs.com/oauth/request_token"
DISCOGS_AUTHORIZE_URL = "https://www.discogs.com/oauth/authorize"
DISCOGS_ACCESS_TOKEN_URL = "https://api.discogs.com/oauth/access_token"


def get_discogs_client() -> discogs_client.Client:
    settings = DiscogsSettings()
    return discogs_client.Client("deepcuts/1.0", user_token=settings.user_token)


# def _get_artists_from_discogs_artists(discogs_artists: list[discogs_client.Artist]) -> list[DiscogsArtist]:
#     """Get a list of Artist models from Discogs artists."""
#     artists = []
#     for discogs_artist in discogs_artists:
#         artists.append(
#             DiscogsArtist(
#                 name=discogs_artist.name,
#                 id=discogs_artist.id,
#                 name_variations=discogs_artist.name_variations if discogs_artist.name_variations else [],
#                 profile=discogs_artist.profile,
#                 image_url=discogs_artist.images[0]["uri"] if discogs_artist.images else None,
#                 role=discogs_artist.role,
#                 url=discogs_artist.url,
#             )
#         )
#     return artists


# def get_tracks_from_release_id(release_id: int) -> list[DiscogsTrack]:
#     """Get tracks from a Discogs release."""
#     client = _get_discogs_client()
#     release = client.release(release_id)
#     tracks = []
#     for track in release.tracklist:
#         tracks.append(
#             DiscogsTrack(
#                 title=track.title,
#                 duration=track.duration,
#                 position=track.position,
#                 artists=_get_artists_from_discogs_artists(track.artists),
#                 credits=_get_artists_from_discogs_artists(track.credits),
#             )
#         )
#     return tracks


def _get_main_release_id(client, title, artist, per_page):
    results = client.search(
        release_title=title, artist=artist, type="master", sort="year", order="desc", per_page=per_page
    )
    for release in results:
        if release.main_release.title == title:
            log.info(f"Found release {release.title} ({release.main_release.id})")
            return release.main_release.id
        log.debug(f"Skipping release {release.title} ({release.main_release.id})")

    raise ValueError(f"Release not found for {title} by {artist}")


def search_for_release(title: str, artist: str | None = None, per_page: int = 20) -> Album:
    """Search for a release on Discogs."""
    client = get_discogs_client()
    release_id = _get_main_release_id(client, title, artist, per_page)
    release = client.release(id=str(release_id))

    start_time = time.time()
    album = Album(
        title=release.title,
        artist_name=artist,
        discogs_release_id=release_id,
        image_url=release.images[0]["uri"],
        credit_artist_ids=[artist.id for artist in release.credits],
    )
    end_time = time.time()
    log.info(f"Fetched release info for {title} ({release.id}) in {end_time - start_time:.2f} seconds")

    return album


def get_release_credits(release_id: int) -> dict[str, Artist]:  # TODO make this accept release objects and print name
    client = get_discogs_client()
    release = client.release(str(release_id))
    log.info(f"Found {len(release.credits)} credits for release {release.title} ({release_id=})")
    artists = {}
    for artist in release.credits:
        image_url = artist.images[0]["uri"] if artist.images else None
        artists[artist.id] = Artist(
            name=artist.name, discogs_artist_id=artist.id, image_url=image_url, role=artist.role
        )
    return artists


def get_artist_albums(artist_id: int) -> list[Album]:
    client = get_discogs_client()
    artist = client.artist(artist_id)
    try:
        log.info(f"Found {len(artist.releases)} releases for artist {artist.name} ({artist_id=})")
        albums = []
        for i, release in enumerate(artist.releases):
            albums.append(Album(title=release.title, artist_name=artist.name, discogs_release_id=release.id))
            if i == 1000:
                break
        return albums
    except Exception as e:
        log.error(e)
        return []


def save_my_albums(filename: str):
    """Save a mock collection of Discogs releases."""
    my_collection = []
    for title, artist in [
        ("To Pimp A Butterfly", "Kendrick Lamar"),
        ("Cosmogramma", "Flying Lotus"),
        ("Kid A", "Radiohead"),
        ("Endtroducing.....", "DJ Shadow"),
        ("The College Dropout", "Kanye West"),
        ("The Chronic", "Dr. Dre"),
        ("The Marshall Mathers LP", "Eminem"),
        ("The Miseducation of Lauryn Hill", "Lauryn Hill"),
        ("Tread", "Ross From Friends"),
        ("Turn On The Bright Lights", "Interpol"),
        ("Either / Or", "Elliott Smith"),
        ("Kid A", "Radiohead"),
        ("Capacity", "Big Thief"),
        ("The Idler Wheel...", "Fiona Apple"),
        ("The ArchAndroid", "Janelle Monáe"),
        ("Dragon New Warm Mountain I Believe In You", "Big Thief"),
        ("The Suburbs", "Arcade Fire"),
        ("Jassbusters", "Connann Mockasin"),
        ("Bravado", "Kirin J Callinan"),
        ("Con Todo El Mundo", "Khruangbin"),
        ("Donuts", "J Dilla"),
        ("It Is What It Is", "Thundercat"),
        ("Homogenic", "Björk"),
        ("Voodoo", "D'Angelo"),
        ("Fatigue", "L'Rain"),
        ("Grinning Cat", "Susumu Yokota"),
        ("Metaphorical Music", "Nujabes"),
        ("Modal Soul", "Nujabes"),
        ("Spiritual State", "Nujabes"),
        ("BRAT", "Charlie XCX"),
    ]:
        try:
            my_collection.append(search_for_release(title, artist))
        except ValueError as e:
            log.error(e)
            continue

    with open(filename, "wb") as handle:
        pickle.dump(my_collection, handle, protocol=pickle.HIGHEST_PROTOCOL)
        log.info(f"Saved {len(my_collection)} albums to {filename}")


def get_artist_albums_by_artist_id(artist_id: int):
    client = get_discogs_client()
    artist = client.artist(artist_id)
    log.info(f"Found {len(artist.releases)} releases for artist {artist.name} ({artist_id=})")
    albums = []
    for release in artist.releases:
        albums.append(Album(title=release.title, artist_name=artist.name, discogs_release_id=release.id))
    return albums


if __name__ == "__main__":
    save_my_albums("my_albums.pkl")
    # client = _get_discogs_client()
    # release = client.release("7557957")
    # release = search_for_release("To Pimp A Butterfly", "Kendrick Lamar")
    # with open("my_collection.pkl", "rb") as handle:
    # my_collection = pickle.load(handle)

    # release = my_collection[0]

    # print(get_artist_albums_by_artist_id(artist_id=release.credits[0].id))  # TODO Fix
