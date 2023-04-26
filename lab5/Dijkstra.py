import sys


def dijkstra(graph):
    start = 0
    num_of_vertices = len(graph)
    visited_and_distance = [[0, start]]

    for i in range(num_of_vertices - 1):
        visited_and_distance.append([0, sys.maxsize])

    for vertex in range(num_of_vertices):

        to_visit = -1
        for index in range(num_of_vertices):
            if visited_and_distance[index][0] == 0 and (to_visit == -1 or
                                                        visited_and_distance[index][1] < visited_and_distance[to_visit][1]):
                to_visit = index

        for neighbor_index in range(num_of_vertices):
            distance = graph[to_visit][neighbor_index]
            new_distance = visited_and_distance[to_visit][1] + distance

            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance

        visited_and_distance[to_visit][0] = 1

