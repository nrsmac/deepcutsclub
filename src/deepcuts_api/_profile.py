"""Profiling performance."""

from cProfile import Profile
from pstats import (
    SortKey,
    Stats,
)

from deepcuts_api.discogs import (
    _get_discogs_client,
    search_for_release,
)

with Profile() as profile:
    client = _get_discogs_client()
    results = search_for_release(client, "To Pimp A Butterfly", artist="Kendrick Lamar")
    (Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats())
