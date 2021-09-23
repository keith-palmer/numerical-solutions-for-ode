from eulers_method import eulers
from runge_kutta_3 import rk3
from runge_kutta_4 import rk4
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
w1 = eulers(func='y-x', a=0, b=10, y=[2], N=99)
w2 = rk3(func='y-x', a=0, b=10, y=[2], N=99)
w3 = rk4(func='y-x', a=0, b=10, y=[2], N=99)
y = x + np.exp(x) + 1

fig, ax = plt.subplots()
ax.plot(x, w1, label="Euler's")
ax.plot(x, w2, label="rk3")
ax.plot(x, w3, label="rk4")
ax.plot(x, y, label="Exact")
ax.legend()
plt.show()
