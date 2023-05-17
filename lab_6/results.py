from tabulate import tabulate
import time
import matplotlib.pyplot as plt


def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nth number')
    plt.ylabel('Time (s)')
    plt.title(name)
    plt.show()
    print(tabulate([['Time (s)'] + y], headers=(['Size'] + x), tablefmt='orgtbl'))


def time_algorithm(algorithm, nth_num):
    start_time = time.time()
    algorithm(nth_num)
    end_time = time.time()
    return end_time - start_time
