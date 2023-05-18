from lab5.denseGraph import generate_dense_graph
from lab5.sparseGraph import generate_sparse_graph
from prims_algorithm import *
from kruskal_algorithm import *
from lab_6.results import *


x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = []
y2 = []
y3 = []
y4 = []

for j in x:
    dense = generate_dense_graph(j)
    sparse = generate_sparse_graph(j)
    # y1.append(time_algorithm(prim, dense))
    # y2.append(time_algorithm(prim, sparse))
    y3.append(time_algorithm(kruskal, dense))
    y4.append(time_algorithm(kruskal, sparse))

# results(x, y4, "Kruskal's of a Sparse Graph")


# plt.plot(x, y1, label="dense_prims", color="r")
# plt.plot(x, y2, label="sparse_prims", color="g")
plt.plot(x, y3, label="dense_kruskal", color="b")
plt.plot(x, y4, label="sparse_kruskal", color="k")

plt.title("Algorithms")
plt.xlabel('Size of the graph')
plt.ylabel('Time Complexity (s)')
plt.legend()
plt.show()

