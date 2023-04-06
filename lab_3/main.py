# # from algorithm1 import *
# # from algorithm2 import *
# # from algorithm3 import *
# # from algorithm4 import *
# # from algorithm5 import *
# # import matplotlib.pyplot as plt
# # from tabulate import tabulate
# # import time
# #
# # x = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# # y1 = []
# # y2 = []
# # y3 = []
# # y4 = []
# # y5 = []
# #
# # def results(x, y, name):
# #     plt.plot(x, y)
# #     plt.xlabel('nr of elements in array')
# #     plt.ylabel('Time (s)')
# #     plt.title(name)
# #     plt.show()
# #     print(tabulate([['Time (s)'] + y], headers=(['nr'] + x), tablefmt='orgtbl'))
# #
# # def time_algorithm(algorithm, size):
# #     start_time = time.time()
# #     algorithm(size)
# #     end_time = time.time()
# #     return end_time - start_time
# #
# #
# # for j in x:
# #     y1.append(time_algorithm(sieve_of_eratosthenes_1, j))
# #     y2.append(time_algorithm(sieve_of_eratosthenes_2, j))
# #     y3.append(time_algorithm(sieve_of_eratosthenes_3, j))
# #     y4.append(time_algorithm(sieve_of_eratosthenes_4, j))
# #     y5.append(time_algorithm(sieve_of_eratosthenes_5, j))
# #
# # results(x, y1, sieve_of_eratosthenes_1.__name__)
# # results(x, y2, sieve_of_eratosthenes_2.__name__)
# # results(x, y3, sieve_of_eratosthenes_3.__name__)
# # results(x, y4, sieve_of_eratosthenes_4.__name__)
# # results(x, y5, sieve_of_eratosthenes_5.__name__)
# #
# # plt.plot(x, y1, label="algorithm1", color = "r")
# # plt.plot(x, y2, label="algorithm2", color = "g")
# # plt.plot(x, y3, label="algorithm3", color = "b")
# # plt.plot(x, y4, label="algorithm4", color = "k")
# # plt.plot(x, y5, label="algorithm5", color = "y")
# #
# # plt.title("Algorithms")
# # plt.xlabel('Length of the array')
# # plt.ylabel('Time Complexity (s)')
# # plt.legend()
# # plt.show()
#
#
# # A Huffman Tree Node
#
# import heapq
#
#
# class node:
#
#     def __init__(self, freq, symbol, left=None, right=None):
#         # frequency of symbol
#
#         self.freq = freq
#
#         # symbol name (character)
#
#         self.symbol = symbol
#
#         # node left of current node
#
#         self.left = left
#
#         # node right of current node
#
#         self.right = right
#
#         # tree direction (0/1)
#
#         self.huff = ''
#
#     def __lt__(self, nxt):
#         return self.freq < nxt.freq
#
#
# # utility function to print huffman
# # codes for all symbols in the newly
# # created Huffman tree
#
# def printNodes(node, val=''):
#     # huffman code for current node
#
#     newVal = val + str(node.huff)
#
#     # if node is not an edge node
#
#     # then traverse inside it
#
#     if (node.left):
#         printNodes(node.left, newVal)
#
#     if (node.right):
#         printNodes(node.right, newVal)
#
#         # if node is edge node then
#
#         # display its huffman code
#
#     if (not node.left and not node.right):
#         print(f"{node.symbol} -> {newVal}")
#
#
# # characters for huffman tree
#
# chars = ['a', 'b', 'c', 'd', 'e', 'f']
#
# # frequency of characters
#
# freq = [3, 5, 10, 7, 20, 12]
#
# # list containing unused nodes
#
# nodes = []
#
# # converting characters and frequencies
# # into huffman tree nodes
#
# for x in range(len(chars)):
#     heapq.heappush(nodes, node(freq[x], chars[x]))
#
# while len(nodes) > 1:
#     # sort all the nodes in ascending order
#
#     # based on their frequency
#
#     left = heapq.heappop(nodes)
#
#     right = heapq.heappop(nodes)
#
#     # assign directional value to these nodes
#
#     left.huff = 0
#
#     right.huff = 1
#
#     # combine the 2 smallest nodes to create
#
#     # new node as their parent
#
#     newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
#
#     heapq.heappush(nodes, newNode)
#
# # Huffman Tree is ready!
#
# printNodes(nodes[0])


# Floyd Warshall Algorithm in python


# The number of vertices
nV = 5

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)


# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G =     [[0, 1, INF, INF, INF],
         [INF, 0, 9, 5, 7],
         [3, INF, 0, 2, INF],
         [INF, INF, INF, 0, INF],
         [INF, INF, INF, 2, 0]]
floyd_warshall(G)
