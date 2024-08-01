"""API routes for the files API."""

from fastapi import (
    APIRouter,
    HTTPException,
)
from loguru import logger as log

from deepcuts_api import spotify
from deepcuts_api.genres import Genre
from deepcuts_api.schemas import (
    Album,
    Artist,
    GetArtistAlbumsResponse,
    GetRecommendationResponse,
)

ROUTER = APIRouter(tags=["deepcuts"])


@ROUTER.get(
    "/albums/{artist_name}", responses={200: {"model": GetArtistAlbumsResponse}, 404: {"description": "Not found"}}
)
async def get_albums_by_artist(artist_name: str) -> GetArtistAlbumsResponse:
    """Get albums by artist name."""
    if albums := spotify.get_albums_by_artist(artist_name):
        return GetArtistAlbumsResponse(albums=albums)
    raise HTTPException(status_code=404, detail="No albums found for artist.")


@ROUTER.post(
    "/recommend",
    responses={
        200: {"model": GetRecommendationResponse},
        400: {"description": "Bad request"},
        404: {"description": "Not found"},
    },
)
async def recommend_albums_from_albums(
    album_titles: list[str] | None, artist_names: list[str] | None, genres: list[Genre] | None = None
) -> GetRecommendationResponse:
    """Recommend albums based on shared artists."""
    log.info(f"Received request with albums: {album_titles}, artists: {artist_names}, genres: {genres}")
    if not album_titles and not artist_names:
        raise HTTPException(status_code=400, detail="At least one of albums or artists each must be provided.")
    artists = [Artist(name=artist_name) for artist_name in artist_names]
    albums = [Album(title=album_title) for album_title in album_titles]
    if recommendations := spotify.get_recommendations(artists=artists, albums=albums, genres=genres):
        return GetRecommendationResponse(albums=recommendations)
    raise HTTPException(status_code=404, detail="No recommendations found.")
