from typing import List
import sys


def dfs(adj: List[List[int]], color: List[int], u: int) -> bool:
    color[u] = 1
    for v in adj[u]:
        if not color[v]:
            if dfs(adj, color, v):
                return True
        elif color[v] == 1:
            return True
    color[u] = -1
    return False


def acyclic(adj: List[List[int]]) -> bool:
    # 0: white, 1:gray, -1:black
    color = [0] * len(adj)

    for i in range(len(adj)):
        if not color[i]:
            if dfs(adj, color, i):
                return True

    return False


def DFS(adj: List[List[int]], color: List[int], order: List[int], u: int) -> None:
    color[u] = 1
    for v in adj[u]:
        if not color[v]:
            DFS(adj, color, order, v)
    color[u] = -1
    order.append(u)


def toposort(adj: List[List[int]]) -> List[int]:
    color = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if not color[i]:
            DFS(adj, color, order, i)
    order.reverse()
    return order


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x - 1].append(y - 1)

if not acyclic(adj):
    order = toposort(adj)

    for i in range(len(order)):
        print(order[i] + 1, end=" ")
    print()
else:
    print("The graph is not acyclic, cannot find a topological order.")
