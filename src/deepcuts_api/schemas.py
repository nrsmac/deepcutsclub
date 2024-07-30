"""Pydantic schemas for the files API."""

from pydantic import BaseModel

DEFAULT_GET_PAGE_SIZE = 10
DEFAULT_GET_MIN_PAGE_SIZE = 10
DEFAULT_GET_MAX_PAGE_SIZE = 100


class Album(BaseModel):
    """Schema for an album."""

    title: str
    artist_name: str
    discogs_release_id: int
    image_url: str | None = None
    credit_artist_ids: list[int] = []  # List of album credits
    album_ids: list[int] | None = None


class Artist(BaseModel):
    """Schema for an artist."""

    name: str
    discogs_artist_id: int
    image_url: str | None = None
    role: str | None = None
    albums: list[Album] = []


class GetArtistAlbumsResponse(BaseModel):
    """Schema for an album_response."""

    albums: list[Album]
