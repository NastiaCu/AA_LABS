import heapq
from typing import List, Tuple

INF = float("inf")


def dijkstra(n: int, edges: List[List[Tuple[int, int]]], start: int, end: int) -> int:
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if u == end:
            return d
        if dist[u] < d:
            continue
        for v, w in edges[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return -1


n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
start, end = map(int, input().split())
print(dijkstra(n, edges, start, end))
