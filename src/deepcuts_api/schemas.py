"""Pydantic schemas for the files API."""


from pydantic import BaseModel

DEFAULT_GET_PAGE_SIZE = 10
DEFAULT_GET_MIN_PAGE_SIZE = 10
DEFAULT_GET_MAX_PAGE_SIZE = 100


class AlbumImageMetadata(BaseModel):
    """Schema for album image metadata."""

    height: int
    width: int
    url: str


class Album(BaseModel):
    """Schema for an album."""

    name: str
    artists: list[str]
    release_date: str
    total_tracks: int
    tracks: list[str]
    image: AlbumImageMetadata
    spotify_url: str


class GetAlbumsResponse(BaseModel):
    """Schema for an album_response."""

    albums: list[Album]

