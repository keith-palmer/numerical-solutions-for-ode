from function_parser import func_parser
import numpy as np

def rk4(func, a, b, y, N):
    '''
    Function apporximates y(x) using Runge-Kutta 4 at various mesh point along the interval [a,b].
    Example function is y' = f(x,y) = y - x where parameter func would be y - x.
    Parameters: func, initial (a) and final (b) points of interval, initial y (as list), N (number of steps)
    '''
    h = (b - a) / N
    x = np.linspace(a, b, N+1)

    for n in range(N):
        k1 = h * func_parser(func, y[n], x[n])
        k2 = h * func_parser(func, (y[n] + 0.5*k1), (x[n] + 0.5*h))
        k3 = h * func_parser(func, (y[n] + 0.5*k2), (x[n] + 0.5*h))
        k4 = h * func_parser(func, (y[n] + k3), (x[n] + h))
        y_next = y[n] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        y.append(round(y_next, 15))
    return y
