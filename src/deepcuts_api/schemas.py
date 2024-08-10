"""Pydantic schemas for the files API."""

from pydantic import BaseModel

DEFAULT_GET_PAGE_SIZE = 10
DEFAULT_GET_MIN_PAGE_SIZE = 10
DEFAULT_GET_MAX_PAGE_SIZE = 100


class Album(BaseModel):
    """Schema for an album."""

    title: str
    artist_name: str | None = None
    spotify_id: str | None = None
    spotify_url: str | None = None
    discogs_release_id: int | None = None
    image_url: str | None = None
    credit_artist_ids: list[int] = []  # List of album credits


class Artist(BaseModel):
    """Schema for an artist."""

    name: str
    spotify_id: str | None = None
    discogs_artist_id: int | None = None
    image_url: str | None = None
    role: str | None = None
    albums: list[Album] = []


class GetArtistAlbumsResponse(BaseModel):
    """Schema for an album_response."""

    albums: list[Album]


class RecommendAlbumsQueryParams(BaseModel):
    """Schema for a recommendation query parameters."""

    album_titles: list[str] = []
    artist_names: list[str] = []
    genres: list[str] = []


class GetRecommendationResponse(BaseModel):
    """Schema for a recommendation response."""

    albums: list[Album]
