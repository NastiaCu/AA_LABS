import random
import numpy as np


def generate_dense_graph(num_nodes):
    graph = np.full((num_nodes, num_nodes), np.inf)
    np.fill_diagonal(graph, 0)
    connected = False
    while not connected:
        start_node = random.randint(0, num_nodes - 1)
        visited = [start_node]
        while len(visited) < num_nodes:
            unvisited = [node for node in range(num_nodes) if node not in visited]
            random.shuffle(unvisited)
            for node in unvisited:
                if graph[node][visited[-1]] == np.inf:
                    graph[node][visited[-1]] = graph[visited[-1]][node] = random.randint(1, 10)
                    visited.append(node)
                    break
            else:
                break
        else:
            connected = True

    max_num_edges = int((num_nodes * (num_nodes - 1)) / 2)
    num_edges = random.randint(num_nodes - 1, max_num_edges)
    edges = [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes)]
    random.shuffle(edges)
    for i, j in edges[:num_edges]:
        graph[i][j] = graph[j][i] = random.randint(1, 10)

    return graph.tolist()

