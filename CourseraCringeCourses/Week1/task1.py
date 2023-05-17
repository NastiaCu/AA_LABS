def DFS(graph, u, v, visited):
    if u == v:
        return True
    visited[u] = True
    for neighbor in graph[u]:
        if not visited[neighbor]:
            if DFS(graph, neighbor, v, visited):
                return True
    return False


def is_reachable():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    u, v = map(int, input().split())
    visited = [False] * (n+1)

    if DFS(graph, u, v, visited):
        print(1)
    else:
        print(0)

is_reachable()
