from tabulate import tabulate
import time
import matplotlib.pyplot as plt


def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('Size of the Graph')
    plt.ylabel('Time (s)')
    plt.title(name)
    plt.show()
    print(tabulate([['Time (s)'] + y], headers=(['Size'] + x), tablefmt='orgtbl'))


def time_algorithm(algorithm, graph):
    start_time = time.time()
    algorithm(graph)
    end_time = time.time()
    return end_time - start_time
