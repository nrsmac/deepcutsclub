"""API routes for the files API."""

from fastapi import APIRouter

from deepcuts_api import spotify
from deepcuts_api.schemas import GetArtistAlbumsResponse

ROUTER = APIRouter(tags=["Files"])


@ROUTER.get("/albums/{artist_name}", response_model=GetArtistAlbumsResponse)
async def get_album(artist_name: str):
    """Get albums by artist name."""
    if albums := spotify.get_albums_by_artist(artist_name):
        return GetArtistAlbumsResponse(albums=albums)
