def floyd_warshall(graph):
    num_of_vertices = len(graph)
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(num_of_vertices):
        for i in range(num_of_vertices):
            for j in range(num_of_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

