from function_parser import func_parser
import numpy as np

def rk3(func, a, b, y, N):
    '''
    Function apporximates y(x) using Runge-Kutta 3 method along the interval [a,b].

    Args:
        func:  Function to be estimated.  Example; y' = f(x,y) = y - x.
        a: Initial point
        b: Final point
        y: List containg the initial value of y.
        N: Number of desired steps.

    Returns:
       y:  List of values of y_i
    '''

    h = (b - a) / N
    x = np.linspace(a, b, N+1)

    for n in range(N):
        k1 = h * func_parser(func, y[n], x[n])
        k2 = h * func_parser(func, (y[n] + 0.5*k1), (x[n] + 0.5*h))
        k3 = h * func_parser(func, (y[n] - k1 + 2*k2), (x[n] + h))
        y_next = y[n] + (1/6) * (k1 + 4*k2 + k3)
        y.append(round(y_next, 15))
    return y
