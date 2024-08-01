import json
import random

from loguru import logger as log
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from deepcuts_api.collection import my_collection
from deepcuts_api.schemas import Album
from deepcuts_api.settings import SpotifySettings

settings = SpotifySettings()


client = Spotify(
    retries=0,
    auth_manager=SpotifyClientCredentials(client_id=settings.client_id, client_secret=settings.client_secret),
)


sample_albums = random.sample(my_collection, 5)


seed_artists = [album.artist_name for album in sample_albums]
seed_albums = [album.title for album in sample_albums]
log.info(f"Sample albums: {[album.title for album in sample_albums]}")

seed_artist_ids = [client.search(q=artist, type="artist")["artists"]["items"][0]["id"] for artist in seed_artists]
seed_album_ids = [client.search(q=album, type="album")["albums"]["items"][0]["id"] for album in seed_albums]

genres = list(client.recommendation_genre_seeds().items())
log.info(f"Available genres: {genres}")

recommendations = client.recommendations(seed_artists=seed_artist_ids, seed_albums=seed_album_ids, genres=genres)

recommended_albums: list[Album] = []
for reccomendation in recommendations["tracks"]:
    recommended_albums.append(
        Album(
            title=reccomendation["album"]["name"],
            artist_name=reccomendation["album"]["artists"][0]["name"],
            spotify_id=reccomendation["album"]["id"],
            image_url=reccomendation["album"]["images"][0]["url"],
        )
    )

with open("recommended_albums.json", "w", encoding="utf-8") as f:
    f.write(json.dumps([album.model_dump() for album in recommended_albums], indent=2))
