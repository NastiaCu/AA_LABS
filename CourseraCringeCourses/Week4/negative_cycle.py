def negative_cycle(adj, cost):
    dist = [0] * len(adj)

    for i in range(len(adj) - 1):
        for u in range(len(adj)):
            for j in range(len(adj[u])):
                v = adj[u][j]
                if dist[v] > dist[u] + cost[u][j]:
                    dist[v] = dist[u] + cost[u][j]

    for u in range(len(adj)):
        for j in range(len(adj[u])):
            v = adj[u][j]
            if dist[v] > dist[u] + cost[u][j]:
                return 1

    return 0


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    adj[a - 1].append(b - 1)
    cost[a - 1].append(w)

print(negative_cycle(adj, cost))
