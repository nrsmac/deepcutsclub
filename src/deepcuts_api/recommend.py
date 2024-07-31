import pickle

import networkx as nx
import plotly.graph_objects as go
from loguru import logger as log
from tqdm import tqdm

from deepcuts_api.discogs import discogs
from deepcuts_api.schemas import (
    Album,
    Artist,
)


def create_album_graph(
    my_albums: list[Album], credits_: dict[str, dict[str, Artist]], albums_layer_1: dict[str, list[Album]]
) -> nx.Graph:
    """Create a bipartite graph from album data."""
    # Create a bipartite graph
    graph = nx.Graph()

    # Add nodes with the node attribute "bipartite" and album name
    for album in tqdm(my_albums):
        graph.add_node(
            album.discogs_release_id,
            bipartite=0,
            label=f"{album.title} by {album.artist_name}",
            album=album,
        )
        # Add edges between albums with shared artists
        for artist_id in album.credit_artist_ids:
            album_credits = credits_.get(album.discogs_release_id, {})
            for artist_id, _artist in album_credits.items():
                for album2 in albums_layer_1.get(artist_id, []):
                    graph.add_node(
                        album2.discogs_release_id,
                        bipartite=1,
                        label=f"{album.title} by {album.artist_name}",
                        album=album2,
                    )
                    # graph.add_edge(
                    #     album.discogs_release_id,
                    #     album2.discogs_release_id,
                    #     artist=artist,
                    #     label=f"{artist.name} ({artist.role})",
                    # )

        #         for album2 in artist_albums:
        #             if album1.discogs_id != album2.discogs_id:
        #                 graph.add_edge(album1.discogs_id, album2.discogs_id, artist=f"{artist.name} ({artist.role})")
        #                 # graph.add_edge(album.discogs_id, album_id, )

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
        artist_name = edge_attrs.get("label", "Unknown Artist")
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
        title = data.get("label", "Unknown Album")
        node_text.append(title)
        node_annotations.append(
            dict(
                x=x,
                y=y,
                text=title,
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
    discogs.save_my_albums("my_albums.pkl")

    with open("my_albums.pkl", "rb") as handle:
        my_albums = pickle.load(handle)

    # Get all artists from this collection

    credits_by_album_id = {
        album.discogs_release_id: discogs.get_release_credits(release_id=album.discogs_release_id)
        for album in my_albums
    }

    with open("my_album_credits.pkl", "wb") as handle:
        pickle.dump(credits_by_album_id, handle)

    # with open("my_album_credits.pkl", "rb") as handle:
    #     credits_by_album_id = pickle.load(handle)

    core_artists = set()
    for album_id in set(credits_by_album_id.keys()):
        for artist in credits_by_album_id[album_id].values():
            core_artists.add(artist.discogs_artist_id)

    log.info(f"{len(core_artists)} core artists found in collection")

    print([credit for credit in credits_by_album_id.values() if credit])

    # Get all albums for each core artist

    artist_albums_layer_1 = {}
    for i, (album_id, album_credits) in enumerate(tqdm(credits_by_album_id.items())):
        for artist_id in album_credits:
            if artist_id not in artist_albums_layer_1:
                artist_albums_layer_1[artist_id] = discogs.get_artist_albums(artist_id)

    with open("albums_layer_1.pkl", "wb") as handle:
        pickle.dump(artist_albums_layer_1, handle)

        # with open("albums_layer_1.pkl", "rb") as handle:
        #     artist_albums_layer_1 = pickle.load(handle)

    with open("albums_layer_1.pkl", "rb") as handle:
        artist_albums_layer_1 = pickle.load(handle)

    g = create_album_graph(my_albums=my_albums, credits_=credits_by_album_id, albums_layer_1=artist_albums_layer_1)
    with open("album_graph.pkl", "wb") as handle:
        pickle.dump(g, handle)

    # plot_album_graph(g)
