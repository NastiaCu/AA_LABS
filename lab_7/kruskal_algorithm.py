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

