from eulers_method import eulers
from runge_kutta_3 import rk3
from runge_kutta_4 import rk4
import numpy as np

print(eulers(func='y-x',
             a=0,
             b=10,
             y=[2],
             N=100))
print()
print(rk3(func='y-x',
             a=0,
             b=10,
             y=[2],
             N=100))
print()
print(rk4(func='y-x',
             a=0,
             b=10,
             y=[2],
             N=100))
