import heapq
import numpy as np
import random

def prim(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    min_heap = [(0, 0)]  # start with node 0 with 0 weight
    mst_weight = 0
    mst = []

    while min_heap:
        # Get the node with the smallest edge weight
        weight, node = heapq.heappop(min_heap)

        if visited[node]:
            continue

        # Add the node to the MST
        visited[node] = True
        mst_weight += weight

        # Add the edge to the MST
        if node != 0:
            mst.append((node, parent))
        parent = node

        # Add the neighbors to the heap
        for neighbor, weight in enumerate(graph[node]):
            if weight != np.inf and not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor))

    return mst, mst_weight


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

mst = prim(graph)
print(mst)
