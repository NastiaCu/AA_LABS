def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for node in graph[start] - visited:
        dfs(graph, node, visited)
    return visited

