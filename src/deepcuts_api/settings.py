"""Settings for Deepcuts API."""

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


def _get_version_from_file() -> str:
    """Get the version from the `version.txt` file."""
    with open("version.txt", "r", encoding="utf-8") as version_file:
        version = version_file.read().strip()
    return version


class WikipediaSettings(BaseSettings):
    """Settings for the Wikipedia API."""

    wikipedia_client_id: str = Field(...)
    wikipedia_client_secret: str
    wikipedia_access_token: str
    model_config = SettingsConfigDict(case_sensitive=False, env_file=".env", env_prefix="WIKIPEDIA_")


class SpotifySettings(BaseSettings):
    """Settings for the Spotify API."""

    client_id: str = Field(...)
    client_secret: str = Field(...)
    model_config = SettingsConfigDict(case_sensitive=False, env_file=".env", env_prefix="SPOTIFY_", extra="ignore")


class DiscogsSettings(BaseSettings):
    """Settings for the Discogs API."""

    user_token: str = Field(...)
    consumer: str = Field(...)
    consumer_secret: str = Field(...)
    model_config = SettingsConfigDict(case_sensitive=False, env_file=".env", env_prefix="DISCOGS_", extra="ignore")


class Settings(BaseSettings):
    """Settings for the Deepcuts API."""

    version: str = Field(default_factory=_get_version_from_file)

    model_config = SettingsConfigDict(case_sensitive=False, env_file=".env", extra="ignore")
