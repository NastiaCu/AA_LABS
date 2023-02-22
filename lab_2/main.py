from random import randint
from heapSort import *
from mergeSort import *
from bubleSort import *
from quickSort import *
import matplotlib.pyplot as plt
from tabulate import tabulate
import time

x = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
y = []


def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('Time (s)')
    plt.title(name)
    plt.show()
    print(tabulate([['Time (s)'] + y], headers=(['nr'] + x), tablefmt='orgtbl'))


def generate_random_array(size, min_val, max_val):
    return [randint(min_val, max_val) for _ in range(size + 200)]


def time_sorting_algorithm(sorting_algorithm, size, A):
    start_time = time.time()
    sorting_algorithm(A)
    end_time = time.time()
    algorithm_name = sorting_algorithm.__name__
    return end_time - start_time

for i in x:
    A = generate_random_array(i, 1, 6000)
    y.append(time_sorting_algorithm(quickSort, i, A))

results(x, y, quickSort.__name__)
