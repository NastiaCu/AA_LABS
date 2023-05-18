import heapq
import numpy as np


def prim(graph):
    global parent
    num_nodes = len(graph)
    visited = [False] * num_nodes
    min_heap = [(0, 0)]
    mst_weight = 0
    mst = []

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        mst_weight += weight

        if node != 0:
            mst.append((node, parent))
        parent = node

        for neighbor, weight in enumerate(graph[node]):
            if weight != np.inf and not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor))

    return mst, mst_weight


