from tabulate import tabulate
import time
import matplotlib.pyplot as plt


def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('Size of the Tree')
    plt.ylabel('Time (s)')
    plt.title(name)
    plt.show()
    print(tabulate([['Time (s)'] + y], headers=(['Size'] + x), tablefmt='orgtbl'))


def time_algorithm(algorithm, tree):
    start_time = time.time()
    algorithm(tree, '1')
    end_time = time.time()
    return end_time - start_time
