from collections import deque


def bfs(adj_list, start, end):
    queue = deque()
    visited = set()

    queue.append((start, 0))
    visited.add(start)

    while queue:
        curr_node, curr_dist = queue.popleft()

        if curr_node == end:
            return curr_dist

        for neighbor in adj_list[curr_node]:
            if neighbor not in visited:
                queue.append((neighbor, curr_dist + 1))
                visited.add(neighbor)

    return -1


n, m = map(int, input().split())
adj_list = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u - 1].append(v - 1)
    adj_list[v - 1].append(u - 1)

start, end = map(int, input().split())
start -= 1
end -= 1

print(bfs(adj_list, start, end))
