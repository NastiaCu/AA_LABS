from dfs import *
from bfs import *
from balanced import *
from unbalanced import *
from results import *


x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = []
y2 = []
y3 = []
y4 = []

for j in x:
    balanced = balanced_tree(j)
    unbalanced = unbalanced_tree(j)
    y1.append(time_algorithm(dfs, balanced))
    y2.append(time_algorithm(dfs, unbalanced))
    y3.append(time_algorithm(bfs, balanced))
    y4.append(time_algorithm(bfs, unbalanced))

# results(x, y1, dfs.__name__)


plt.plot(x, y1, label="balanced_dfs", color="r")
plt.plot(x, y2, label="unbalanced_dfs", color="g")
plt.plot(x, y3, label="balanced_bfs", color="b")
plt.plot(x, y4, label="unbalanced_bfs", color="k")

plt.title("Algorithms")
plt.xlabel('Size of the tree')
plt.ylabel('Time Complexity (s)')
plt.legend()
plt.show()
