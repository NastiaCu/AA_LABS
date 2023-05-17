import queue


def min_charts(stock_data):
    n = len(stock_data)
    k = len(stock_data[0])
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if all([x < y for x, y in zip(stock_data[i], stock_data[j])]):
                adj[i][j] = 1
    matching = [-1] * n
    busy_Right = [False] * n

    def bfs():
        visitedNodes = set()
        q = queue.Queue()
        q.put((1, None))
        visitedNodes.add((1, None))
        path = []
        parent = dict()
        while not q.empty():
            currNode = q.get()
            if 1 == currNode[0]:
                for i in range(n):
                    if -1 == matching[i]:
                        visitedNodes.add((2, i))
                        parent[(2, i)] = currNode
                        q.put((2, i))
            elif 2 == currNode[0]:
                i = currNode[1]
                for j in range(n):
                    if 1 == adj[i][j] and j != matching[i] and not (3, j) in visitedNodes:
                        visitedNodes.add((3, j))
                        parent[(3, j)] = currNode
                        q.put((3, j))
            elif 3 == currNode[0]:
                j = currNode[1]
                if not busy_Right[j]:
                    prevNode = currNode
                    currNode = (4, j)
                    while True:
                        path.insert(0, (prevNode, currNode))
                        if 1 == prevNode[0]:
                            break
                        currNode = prevNode
                        prevNode = parent[currNode]
                    for e in path:
                        if 2 == e[0][0]:
                            matching[e[0][1]] = e[1][1]
                        elif 3 == e[0][0] and 4 == e[1][0]:
                            busy_Right[e[1][1]] = True
                    return True
                else:
                    for i in range(n):
                        if j == matching[i] and not (2, i) in visitedNodes:
                            visitedNodes.add((2, i))
                            parent[(2, i)] = currNode
                            q.put((2, i))
        return False

    while bfs():
        continue
    return len([0 for i in matching if -1 == i])

n, k = map(int, input().split())
stock_data = [list(map(int, input().split())) for i in range(n)]
result = min_charts(stock_data)
print(result)

