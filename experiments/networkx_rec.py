import networkx as nx

sample_data = {
    "Album1": ["Artist1", "Producer1"],
    "Album2": ["Artist2", "Producer1"],
    "Album3": ["Artist1"],
    "Album4": ["Artist3", "Producer2"],
    "Album5": ["Artist1", "Producer2"],
}

# Create a bipartite graph
B = nx.Graph()

# Add nodes with the node attribute "bipartite"
B.add_nodes_from(sample_data.keys(), bipartite=0)

# Add edges between albums and collaborators
for album, collaborators in sample_data.items():
    for collaborator in collaborators:
        B.add_edge(album, collaborator, weight=1)

# Project bipartite graph to album nodes
album_graph = nx.bipartite.weighted_projected_graph(B, sample_data.keys())


# Recommend albums based on common collaborators
def recommend_albums(album, top_n=2):
    neighbors = album_graph[album]
    recommendations = sorted(neighbors, key=lambda x: neighbors[x]["weight"], reverse=True)
    return recommendations[:top_n]


# Example usage
print(recommend_albums("Album5"))
