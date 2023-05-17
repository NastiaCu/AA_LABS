from collections import deque

def bfs(s, t, graph, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[t]

def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(source, sink, graph, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u - 1][v - 1] += c
print(ford_fulkerson(graph, 0, n - 1))
