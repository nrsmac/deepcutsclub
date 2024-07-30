import pickle

import networkx as nx
import plotly.graph_objects as go

from deepcuts_api.discogs import discogs
from deepcuts_api.schemas import (
    Album,
)


def create_album_graph(albums: list[Album]) -> nx.Graph:
    """Create a bipartite graph from album data."""
    # Create a bipartite graph
    graph = nx.Graph()
    albums_by_artist_ids = {}
    for album in albums:
        for artist in album.artists:
            if artist.discogs_id not in albums_by_artist_ids:
                albums_by_artist_ids[artist.discogs_id] = []
            albums_by_artist_ids[artist.discogs_id].append(album)

    # Add nodes with the node attribute "bipartite" and album name
    for album in albums:
        graph.add_node(album.discogs_id, bipartite=0, album=album.name, id=album.discogs_id)

    # Add edges between albums with shared artists
    for album1 in albums:
        for artist in album1.artists:
            artist_albums = albums_by_artist_ids[artist.discogs_id]
            for album2 in artist_albums:
                if album1.discogs_id != album2.discogs_id:
                    graph.add_edge(album1.discogs_id, album2.discogs_id, artist=f"{artist.name} ({artist.role})")
                    # graph.add_edge(album.discogs_id, album_id, )

    return graph


def plot_album_graph(graph: nx.Graph):
    pos = nx.spring_layout(graph)
    edge_x = []
    edge_y = []
    edge_annotations = []
    for edge in graph.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
        # Ensure the artist name is correctly retrieved
        edge_attrs = edge[2]
        artist_name = edge_attrs.get("artist", "Unknown Artist")
        edge_annotations.append(
            dict(
                x=(x0 + x1) / 2,
                y=(y0 + y1) / 2,
                text=artist_name,
                showarrow=False,
                font=dict(color="black", size=10),
                align="center",
            )
        )

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color="#888"), mode="lines")
    node_x = []
    node_y = []
    node_text = []
    node_annotations = []
    for node, data in graph.nodes(data=True):
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        # Ensure the album name is correctly retrieved
        album_name = data.get("album", "Unknown Album")
        node_text.append(album_name)
        node_annotations.append(
            dict(
                x=x,
                y=y,
                text=album_name,
                showarrow=False,
                font=dict(color="black", size=10),
                align="center",
            )
        )

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        hoverinfo="text",
        marker=dict(
            showscale=True,
            colorscale="YlGnBu",
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(thickness=15, title="Node Connections", xanchor="left", titleside="right"),
            line_width=2,
        ),
        text=node_text,
        textposition="top center",
    )

    node_adjacencies = []
    for node, adjacencies in enumerate(graph.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))

    node_trace.marker.color = node_adjacencies

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            showlegend=False,
            hovermode="closest",
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            annotations=edge_annotations + node_annotations,
        ),
    )
    fig.show()


if __name__ == "__main__":
    # Load collection of Albums
    with open("my_albums.pkl", "rb") as handle:
        my_albums = pickle.load(handle)

    client = discogs.get_discogs_client()

    # Get all artists from this collection

    credits = {
        album.discogs_release_id: discogs.get_release_credits(release_id=album.discogs_release_id)
        for album in my_albums
    }
    print(credits)

    # Get core artists
    # core_artists = [get_album_credits(album) for album in albums]

    # Get all albums for each core artist
    # def get_albums_for_artist(artist_id: int) -> list[Album]: ...

    # albums_layer_1 = {artist: get_albums_for_artist(artist) for artist in core_artists}
