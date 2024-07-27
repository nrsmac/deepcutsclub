"""API routes for the files API."""

from fastapi import APIRouter

from deepcuts_api import spotify
from deepcuts_api.schemas import GetAlbumsResponse

ROUTER = APIRouter(tags=["Files"])


@ROUTER.get("/albums/{artist_name}", response_model=GetAlbumsResponse)
async def get_album(artist_name: str):
    """Get albums by artist name."""
    if albums := spotify.get_albums_by_artist(artist_name):
        return GetAlbumsResponse(albums=albums)
