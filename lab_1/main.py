import matplotlib.pyplot as plt
from prettytable import PrettyTable
import math

##Recursive method

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


fibonacci_recursive(7)
fibonacci_recursive(10)
fibonacci_recursive(12)
fibonacci_recursive(15)
fibonacci_recursive(17)
fibonacci_recursive(20)
fibonacci_recursive(22)
fibonacci_recursive(25)
fibonacci_recursive(27)
fibonacci_recursive(30)
fibonacci_recursive(32)
fibonacci_recursive(35)
fibonacci_recursive(37)
fibonacci_recursive(40)
fibonacci_recursive(42)
fibonacci_recursive(45)

time = [0.222, 0.225, 0.222, 0.220, 0.224, 0.219, 0.227, 0.232, 0.254, 0.295, 0.531, 1.009, 3.548, 8.957, 37.498, 97.675]
arr = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42]
plt.plot(arr, time, color='blue', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.ylabel('Time(ms)')
plt.xlabel('n-th Fibonacci Term')

plt.title('Recursive Fibonacci Function')
plt.show()

t = PrettyTable()

t.field_names = ['n-th number', 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42]
t.add_row(['Time(s)', 0.222, 0.225, 0.222, 0.220, 0.224, 0.219, 0.227, 0.232, 0.254, 0.295, 0.531, 1.009, 3.548, 8.957, 37.498, 97.675])
print(t)



##Iterative method

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev1 = 0
        prev2 = 1
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return prev2


fibonacci_iterative(631)
fibonacci_iterative(794)
fibonacci_iterative(1000)
fibonacci_iterative(1259)
fibonacci_iterative(1585)
fibonacci_iterative(1995)
fibonacci_iterative(2512)
fibonacci_iterative(3162)
fibonacci_iterative(3981)
fibonacci_iterative(5012)
fibonacci_iterative(6310)
fibonacci_iterative(7943)
fibonacci_iterative(10000)
fibonacci_iterative(12589)
fibonacci_iterative(15849)


time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.001, 0.001, 0.002, 0.003]
arr = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
plt.plot(arr, time, color='blue', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time(s)')

plt.title('Iterative Method')
plt.show()




##Dynamic programming method

def fibonacci_dp(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


fibonacci_dp(501)
fibonacci_dp(631)
fibonacci_dp(794)
fibonacci_dp(1000)
fibonacci_dp(1259)
fibonacci_dp(1585)
fibonacci_dp(1995)
fibonacci_dp(2512)
fibonacci_dp(3162)
fibonacci_dp(3981)
fibonacci_dp(5012)
fibonacci_dp(6310)
fibonacci_dp(7943)
fibonacci_dp(10000)
fibonacci_dp(12589)
fibonacci_dp(15849)

time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.003, 0.004, 0.007]
arr = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
plt.plot(arr, time, color='blue', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time(s)')

plt.title('Dynamic programming Method')
plt.show()




##Matrix Multiplication method

def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return C


def fibonacci_matrix(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        A = [[1, 1], [1, 0]]
        B = [[1, 1], [1, 0]]
        for i in range(2, n):
            B = matrix_mult(A, B)
        return B[0][0]


time = [0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.002, 0.003, 0.005, 0.013, 0.012, 0.017, 0.031, 0.042, 0.056]
arr = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
plt.plot(arr, time, color='blue', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time(s)')

plt.title('Matrix Multiplication Method')
plt.show()




##Binet formula method


def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))


fibonacci_binet(631)
fibonacci_binet(794)
fibonacci_binet(1000)
fibonacci_binet(1259)
fibonacci_binet(1585)
fibonacci_binet(1995)
fibonacci_binet(2512)
fibonacci_binet(3162)
fibonacci_binet(3981)
fibonacci_binet(5012)
fibonacci_binet(6310)
fibonacci_binet(7943)
fibonacci_binet(10000)
fibonacci_binet(12589)
fibonacci_binet(15849)

time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002, 0.0002, 0.0005]
arr = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
plt.plot(arr, time, color='blue', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time(ms)')

plt.title('Binet Formula Method')
plt.show()




##Tail recursion method

def fibonacci_tail_recursion(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_tail_recursion(n-1, b, a+b)

fibonacci_tail_recursion(631)
fibonacci_tail_recursion(794)
fibonacci_tail_recursion(1000)
fibonacci_tail_recursion(1259)
fibonacci_tail_recursion(1585)
fibonacci_tail_recursion(1995)
fibonacci_tail_recursion(2512)
fibonacci_tail_recursion(3162)
fibonacci_tail_recursion(3981)
fibonacci_tail_recursion(5012)
fibonacci_tail_recursion(6310)
fibonacci_tail_recursion(7943)
fibonacci_tail_recursion(10000)
fibonacci_tail_recursion(12589)
fibonacci_tail_recursion(15849)

time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.001, 0.0012, 0.003, 0.001, 0.001, 0.001, 0.001]
arr = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
plt.plot(arr, time, color='blue', linestyle='dashed', linewidth = 2, marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel('n-th Fibonacci Term')
plt.ylabel('Time(s)')

plt.title('Tail Recursion Method')
plt.show()



t = PrettyTable()

t.field_names = ['Time(s) \ n-th number', 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
t.add_row(['Iterative', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.001, 0.001, 0.002, 0.003])
t.add_row(['Matrix multiplication',0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.002, 0.003, 0.005, 0.013, 0.012, 0.017, 0.031, 0.042, 0.056])
t.add_row(['Dynamic programming', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.003, 0.004, 0.007])
t.add_row(['Binet formula', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002, 0.0002, 0.0005])
t.add_row(['Tail recursion',0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.001, 0.0012, 0.003, 0.001, 0.001, 0.001, 0.001])

print(t)
