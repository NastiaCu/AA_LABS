from nth_decimal_pi_bbp import *
from nth_decimal_pi_chudnovsky import *
from nth_decimal_pi_gl import *
from results import *


x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = []
y2 = []
y3 = []


for j in x:

    y1.append(time_algorithm(nth_decimal_pi_chudnovsky, j))
    y2.append(time_algorithm(nth_decimal_pi_bbp, j))
    y3.append(time_algorithm(nth_decimal_pi_gl, j))


results(x, y3, "Gauss-Legendre")


# plt.plot(x, y1, label="Chudnovsky Algorithm", color="r")
# plt.plot(x, y2, label="Bailey–Borwein–Plouffe Algorithm", color="g")
# plt.plot(x, y3, label="Gauss-Legendre Algorithm", color="b")
#
# plt.title("Algorithms")
# plt.xlabel('nth number')
# plt.ylabel('Time Complexity (s)')
# plt.legend()
# plt.show()
