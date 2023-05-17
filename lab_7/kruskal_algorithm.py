import random
import numpy as np

def kruskal(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] != np.inf:
                edges.append((graph[i][j], i, j))
    edges.sort()

    parent = list(range(n))
    rank = [0] * n
    mst = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        if xroot == yroot:
            return
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v))

    return mst

def generate_sparse_graph(num_nodes):
    graph = np.full((num_nodes, num_nodes), np.inf)
    np.fill_diagonal(graph, 0)
    num_edges = random.randint(num_nodes - 1, num_nodes * (num_nodes - 1) // 4)
    edges = [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)]
    selected_edges = random.sample(edges, num_edges)
    for i, j in selected_edges:
        graph[i][j] = graph[j][i] = random.randint(1, 10)

    for i in range(num_nodes):
        if not any(graph[i]):
            j = random.randint(0, num_nodes-1)
            while j == i:
                j = random.randint(0, num_nodes-1)
            weight = random.randint(1, 10)
            graph[i][j] = graph[j][i] = weight

    return graph.tolist()

graph = generate_sparse_graph(30)
mst = kruskal(graph)
print(mst)

