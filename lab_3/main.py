from algorithm1 import *
from algorithm2 import *
from algorithm3 import *
from algorithm4 import *
from algorithm5 import *
import matplotlib.pyplot as plt
from tabulate import tabulate
import time

x = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

def results(x, y, name):
    plt.plot(x, y)
    plt.xlabel('nr of elements in array')
    plt.ylabel('Time (s)')
    plt.title(name)
    plt.show()
    print(tabulate([['Time (s)'] + y], headers=(['nr'] + x), tablefmt='orgtbl'))

def time_algorithm(algorithm, size):
    start_time = time.time()
    algorithm(size)
    end_time = time.time()
    return end_time - start_time


for j in x:
    y1.append(time_algorithm(sieve_of_eratosthenes_1, j))
    y2.append(time_algorithm(sieve_of_eratosthenes_2, j))
    y3.append(time_algorithm(sieve_of_eratosthenes_3, j))
    y4.append(time_algorithm(sieve_of_eratosthenes_4, j))
    y5.append(time_algorithm(sieve_of_eratosthenes_5, j))
#
# results(x, y1, sieve_of_eratosthenes_5.__name__)
# results(x, y2, sieve_of_eratosthenes_5.__name__)
# results(x, y3, sieve_of_eratosthenes_5.__name__)
# results(x, y4, sieve_of_eratosthenes_5.__name__)
# results(x, y5, sieve_of_eratosthenes_5.__name__)

plt.plot(x, y1, label="algorithm1", color = "r")
plt.plot(x, y2, label="algorithm2", color = "g")
plt.plot(x, y3, label="algorithm3", color = "b")
plt.plot(x, y4, label="algorithm4", color = "k")
plt.plot(x, y5, label="algorithm5", color = "y")

plt.title("Algorithms")
plt.xlabel('Length of the array')
plt.ylabel('Time Complexity (s)')
plt.legend()
plt.show()
