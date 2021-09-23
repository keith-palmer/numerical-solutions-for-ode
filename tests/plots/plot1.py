from eulers_method import eulers
from runge_kutta_3 import rk3
from runge_kutta_4 import rk4
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 11)
w1 = eulers(func='y-x**2+1', a=0, b=2, y=[0.5], N=10)
w2 = rk3(func='y-x**2+1', a=0, b=2, y=[0.5], N=10)
w3 = rk4(func='y-x**2+1', a=0, b=2, y=[0.5], N=10)
y = (x+1)**2 - 0.5*np.exp(x)


fig, ax = plt.subplots()
ax.plot(x, w1, label="Euler's")
ax.plot(x, w2, label="rk3")
ax.plot(x, w3, label="rk4")
ax.plot(x, y, label="Exact")
ax.legend()
plt.show()
