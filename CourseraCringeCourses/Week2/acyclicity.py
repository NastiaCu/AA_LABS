import sys


def is_cyclic_util(v, visited, rec_stack, adj):
    visited[v] = True
    rec_stack[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            if is_cyclic_util(neighbor, visited, rec_stack, adj):
                return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[v] = False
    return False


def is_cyclic(adj):
    visited = [False] * len(adj)
    rec_stack = [False] * len(adj)
    for vertex in range(len(adj)):
        if not visited[vertex]:
            if is_cyclic_util(vertex, visited, rec_stack, adj):
                return 1
    return 0


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)

print(is_cyclic(adj))
