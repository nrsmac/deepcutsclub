from unittest.mock import (
    MagicMock,
    patch,
)

import pytest

from deepcuts_api.discogs.discogs import (
    _get_artists_from_discogs_artists,
    _get_main_release_id,
    get_discogs_client,
    get_tracks_from_release_id,
    search_for_release,
)
from deepcuts_api.discogs.models import (
    DiscogsArtist,
    DiscogsCredit,
    DiscogsLabel,
    DiscogsRelease,
    DiscogsTrack,
)


@patch("deepcuts_api.discogs.discogs.DiscogsSettings")
@patch("discogs_client.Client")
def test_get_discogs_client(mock_client, mock_settings):
    mock_settings.return_value.user_token = "test_token"
    get_discogs_client()
    mock_client.assert_called_once_with("deepcuts/1.0", user_token="test_token")


def test_get_artists_from_discogs_artists():
    mock_artist = MagicMock()
    mock_artist.name = "Artist Name"
    mock_artist.id = 123
    mock_artist.name_variations = ["Artist Name", "A. Name"]
    mock_artist.profile = "Artist Profile"
    mock_artist.images = [{"uri": "http://example.com/image.jpg"}]
    mock_artist.role = "Role"
    mock_artist.url = "http://example.com"

    artists = _get_artists_from_discogs_artists([mock_artist])
    assert len(artists) == 1
    assert artists[0] == DiscogsArtist(
        name="Artist Name",
        id=123,
        name_variations=["Artist Name", "A. Name"],
        profile="Artist Profile",
        image_url="http://example.com/image.jpg",
        role="Role",
        url="http://example.com",
    )


def test_get_tracks_from_release():
    mock_track = MagicMock()
    mock_track.title = "Track Title"
    mock_track.duration = "3:30"
    mock_track.position = "1"
    mock_track.artists = []
    mock_track.credits = []

    mock_release = MagicMock()
    mock_release.tracklist = [mock_track]

    tracks = get_tracks_from_release_id(mock_release)
    assert len(tracks) == 1
    assert tracks[0] == DiscogsTrack(
        title="Track Title",
        duration="3:30",
        position="1",
        artists=[],
        credits=[],
    )


from unittest.mock import (
    MagicMock,
    patch,
)

import pytest

from deepcuts_api.discogs.discogs import (
    get_discogs_client,
    search_for_release,
)
from deepcuts_api.discogs.models import (
    DiscogsCredit,
    DiscogsLabel,
    DiscogsRelease,
    DiscogsTrack,
)


@patch("deepcuts_api.discogs.discogs._get_discogs_client")
@patch("discogs_client.Client")
def test_search_for_release_success(mock_client, mock_get_client):
    mock_release = MagicMock()
    mock_release.id = 1
    mock_release.title = "Radiohead - Amnesiac"
    mock_release.genres = ["Rock"]
    mock_release.styles = ["Alternative Rock"]

    mock_label = MagicMock()
    mock_label.id = 1
    mock_label.name = "Label"
    mock_label.profile = None
    mock_label.urls = []
    mock_label.images = []
    mock_release.labels = [mock_label]

    mock_track = MagicMock()
    mock_track.title = "Track Title"
    mock_track.duration = "3:30"
    mock_track.position = "1"
    mock_track.artists = []
    mock_track.credits = []
    mock_release.tracklist = [mock_track]

    mock_release.url = "http://example.com/release"
    mock_release.images = [{"uri": "http://example.com/image.jpg"}]
    mock_release.data = {
        "extraartists": [
            {"name": "Extra Artist", "role": "Role", "resource_url": "http://example.com", "id": 1, "tracks": ""}
        ]
    }

    mock_master = MagicMock()
    mock_master.title = "Radiohead - Amnesiac"
    mock_master.main_release = mock_release

    mock_client.return_value.search.return_value = [mock_master]
    mock_get_client.return_value = mock_client

    client = get_discogs_client()
    result = search_for_release(client, "Amnesiac", "Radiohead")

    assert isinstance(result, DiscogsRelease)
    assert result.id == 1
    assert result.title == "Radiohead - Amnesiac"
    assert result.genres == ["Rock"]
    assert result.styles == ["Alternative Rock"]
    assert len(result.labels) == 1
    assert isinstance(result.labels[0], DiscogsLabel)
    assert result.labels[0].name == "Label"
    assert len(result.tracks) == 1
    assert isinstance(result.tracks[0], DiscogsTrack)
    assert result.url == "http://example.com/release"
    assert result.image_url == "http://example.com/image.jpg"
    assert len(result.extra_artists) == 1
    assert isinstance(result.extra_artists[0], DiscogsCredit)


@patch("deepcuts_api.discogs.discogs._get_discogs_client")
@patch("discogs_client.Client")
def test_search_for_release_success(mock_client, mock_get_client):
    mock_release = MagicMock()
    mock_release.id = 1
    mock_release.title = "Radiohead - Amnesiac"
    mock_release.genres = ["Rock"]
    mock_release.styles = ["Alternative Rock"]

    mock_label = MagicMock()
    mock_label.id = 1
    mock_label.name = "Label"
    mock_label.profile = None
    mock_label.urls = []
    mock_label.images = []
    mock_release.labels = [mock_label]

    mock_track = MagicMock()
    mock_track.title = "Track Title"
    mock_track.duration = "3:30"
    mock_track.position = "1"
    mock_track.artists = []
    mock_track.credits = []
    mock_release.tracklist = [mock_track]

    mock_release.url = "http://example.com/release"
    mock_release.images = [{"uri": "http://example.com/image.jpg"}]
    mock_release.data = {
        "extraartists": [
            {"name": "Extra Artist", "role": "Role", "resource_url": "http://example.com", "id": 1, "tracks": ""}
        ]
    }

    mock_master = MagicMock()
    mock_master.title = "Radiohead - Amnesiac"
    mock_master.main_release = mock_release

    mock_client.return_value.search.return_value = [mock_master]
    mock_get_client.return_value = mock_client

    client = get_discogs_client()
    result = search_for_release(client, "Amnesiac", "Radiohead")

    assert isinstance(result, DiscogsRelease)
    assert result.id == 1
    assert result.title == "Radiohead - Amnesiac"
    assert result.genres == ["Rock"]
    assert result.styles == ["Alternative Rock"]
    assert len(result.labels) == 1
    assert isinstance(result.labels[0], DiscogsLabel)
    assert result.labels[0].name == "Label"
    assert len(result.tracks) == 1
    assert isinstance(result.tracks[0], DiscogsTrack)
    assert result.url == "http://example.com/release"
    assert result.image_url == "http://example.com/image.jpg"
    assert len(result.extra_artists) == 1
    assert isinstance(result.extra_artists[0], DiscogsCredit)


@patch("discogs_client.Client")
def test_get_main_release_success(mock_client):
    mock_release = MagicMock()
    mock_release.title = "Radiohead - Amnesiac"
    mock_release.main_release = MagicMock(id=1)

    mock_client_instance = mock_client.return_value
    mock_client_instance.search.return_value = [mock_release]

    release = _get_main_release_id(mock_client_instance, "Amnesiac", "Radiohead", "year", 1)
    assert release.id == 1
    mock_client_instance.search.assert_called_once_with(
        query="Amnesiac", artist="Radiohead", type="master", sort="year", per_page=1
    )


@patch("discogs_client.Client")
def test_get_main_release_not_found(mock_client):
    mock_client_instance = mock_client.return_value
    mock_client_instance.search.return_value = []

    with pytest.raises(ValueError, match="Release not found for Amnesiac by Radiohead"):
        _get_main_release_id(mock_client_instance, "Amnesiac", "Radiohead", "year", 1)
    mock_client_instance.search.assert_called_once_with(
        query="Amnesiac", artist="Radiohead", type="master", sort="year", per_page=1
    )


@patch("discogs_client.Client")
def test_get_main_release_multiple(mock_client):
    mock_release1 = MagicMock()
    mock_release1.title = "Radiohead - Amnesiac"
    mock_release1.main_release = MagicMock(id=1)

    mock_release2 = MagicMock()
    mock_release2.title = "Radiohead - Kid A"
    mock_release2.main_release = MagicMock(id=2)

    mock_client_instance = mock_client.return_value
    mock_client_instance.search.return_value = [mock_release2, mock_release1]

    release = _get_main_release_id(mock_client_instance, "Amnesiac", "Radiohead", "year", 1)
    assert release.id == 1
    mock_client_instance.search.assert_called_once_with(
        query="Amnesiac", artist="Radiohead", type="master", sort="year", per_page=1
    )
