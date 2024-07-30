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
    results = client.search(query=title, artist=artist, type="master", sort="year", order="asc", per_page=per_page)
    release_title = f"{artist} - {title}"

    for release in results:
        if release.title == release_title:
            master = release.main_release
            log.info(f"Found release: {release_title}: {master.id=}")
            return master.id
        log.debug(f"Skipping release: {release.title}")
    raise ValueError(f"Release not found for {title} by {artist}")


def search_for_release(title: str, artist: str, per_page: int = 20) -> Album:
    """Search for a release on Discogs."""
    client = get_discogs_client()
    release_id = _get_main_release_id(client, title, artist, per_page)
    _release = client.release(id=str(release_id))

    start_time = time.time()
    album = Album(
        title=_release.title,
        artist_name=artist,
        discogs_release_id=release_id,
        image_url=_release.images[0]["uri"],
        credit_artist_ids=[artist.id for artist in _release.credits],
    )
    end_time = time.time()
    log.info(f"Fetched release info for {_release.id} in {end_time - start_time:.2f} seconds")

    return album


def get_release_credits(release_id: int) -> list[Artist]:
    client = get_discogs_client()
    release = client.release(str(release_id))
    release.credits
    log.info(f"Found {len(release.credits)} credits for release {release_id}")
    artists = []
    for artist in release.credits:
        image_url = artist.images[0]["uri"] if artist.images else None
        artists.append(Artist(name=artist.name, discogs_artist_id=artist.id, image_url=image_url, role=artist.role))
    return artists


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
        ("Miseducation of Lauryn Hill", "Lauryn Hill"),
        ("The Slim Shady LP", "Eminem"),
        # ("Thriller", "Michael Jackson"),
        ("Tread", "Ross From Friends"),
        ("Turn On The Bright Lights", "Interpol"),
        ("Either/Or", "Elliott Smith"),
        ("Kid A", "Radiohead"),
        ("Capacity", "Big Thief"),
        ("The Idler Wheel...", "Fiona Apple"),
        ("The ArchAndroid", "Janelle Monáe"),
        ("Dragon New Warm Mountain I Believe In You", "Big Thief"),
        ("The Suburbs", "Arcade Fire"),
        ("Jazzbusters", "Connann Mockasin"),
        ("Bravado", "Kirin J Callinan"),
        ("Con Todo El Mundo", "Khruangbin"),
        ("Born Like This", "MF DOOM"),
        ("Donuts", "J Dilla"),
        ("It Is What It Is", "Thundercat"),
        ("Homogenic", "Björk"),
        ("Voodoo", "D'Angelo"),
        # ("Destiny", "The Jacksons"),
        ("Fatigue", "L'Rain"),
        ("Grinning Cat", "Susumu Yokota"),
        ("Metaphorical Music", "Nujabes"),
        ("Modal Soul", "Nujabes"),
        ("Spiritual State", "Nujabes"),
        ("Klxuds", "Knxwledge"),
    ]:
        try:
            my_collection.append(search_for_release(title, artist))
        except ValueError as e:
            log.error(e)
            continue

    with open(filename, "wb") as handle:
        pickle.dump(my_collection, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    save_my_albums("my_albums.pkl")
    # client = _get_discogs_client()
    # release = client.release("7557957")
    # release = search_for_release("To Pimp A Butterfly", "Kendrick Lamar")
    # with open("my_collection.pkl", "rb") as handle:
    # my_collection = pickle.load(handle)

    # release = my_collection[0]

    # print(get_artist_albums_by_artist_id(artist_id=release.credits[0].id))  # TODO Fix
