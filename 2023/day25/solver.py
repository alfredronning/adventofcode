import networkx as nx

if __name__ == "__main__":
    graph = open("input.txt").read().strip().split("\n")
    edges = []
    for g in graph:
        fr, to = g.split(": ")
        for t in to.split():
            edges.append((fr, t))

    graph = nx.Graph()
    graph.add_edges_from(edges)

    partition = nx.community.louvain_communities(graph, resolution=0.1)
    print(len(partition[0])*len(partition[1]))

