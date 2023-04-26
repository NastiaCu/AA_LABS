import random
import numpy as np


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

