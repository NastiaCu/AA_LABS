from denseGraph import *
from sparseGraph import *
from FloydWarshall import *
from Dijkstra import *
from results import *


x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = []
y2 = []
y3 = []
y4 = []

for j in x:
    dense = generate_dense_graph(j)
    sparse = generate_sparse_graph(j)
    y1.append(time_algorithm(dijkstra, dense))
    y2.append(time_algorithm(dijkstra, sparse))
    y3.append(time_algorithm(floyd_warshall, dense))
    y4.append(time_algorithm(floyd_warshall, sparse))

# results(x, y4, "Floyd_Warshall of a Sparse Graph")


plt.plot(x, y1, label="dense_dijkstra", color="r")
plt.plot(x, y2, label="sparse_dijkstra", color="g")
plt.plot(x, y3, label="dense_floyd_warshall", color="b")
plt.plot(x, y4, label="sparse_floyd_warshall", color="k")

plt.title("Algorithms")
plt.xlabel('Size of the graph')
plt.ylabel('Time Complexity (s)')
plt.legend()
plt.show()
