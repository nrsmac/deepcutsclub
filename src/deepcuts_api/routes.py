"""API routes for the files API."""

from fastapi import APIRouter

from deepcuts_api import (
    discogs,
    spotify,
)
from deepcuts_api.schemas import GetAlbumsResponse

ROUTER = APIRouter(tags=["Files"])


@ROUTER.get("/albums/{artist_name}", response_model=GetAlbumsResponse)
async def get_album(artist_name: str):
    """Get albums by artist name."""
    if albums := spotify.get_albums_by_artist(artist_name):
        return GetAlbumsResponse(albums=albums)


@ROUTER.get("/album/{artist_name}/{album_name}", response_model=GetAlbumResponse)
async def get_album(artist_name: str, album_name: str):
    """Get album info for an album alongside collaborators."""
    return discogs.search_for_release(artist_name, album_name)
