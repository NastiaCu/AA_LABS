def DFS(graph, u, visited):
    visited[u] = True
    for neighbor in graph[u]:
        if not visited[neighbor]:
            DFS(graph, neighbor, visited)

def connected_components():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n+1)
    count = 0
    for u in range(1, n+1):
        if not visited[u]:
            count += 1
            DFS(graph, u, visited)

    return count

print(connected_components())
