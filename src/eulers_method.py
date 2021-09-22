from function_parser import func_parser
import numpy as np

def eulers(func, a, b, y, N):
    '''
    Function apporximates y(x) using Eulers method at various mesh point along the interval [a,b].
    Example function is y' = f(x,y) = y - x where parameter func would be y - x.
    Parameters: func, initial (a) and final (b) points of interval, initial y (as list), N (number of steps)
    '''
    h = (b - a) / N
    x = np.linspace(a, b, N+1)

    for n in range(N):
        y_next = y[n] + h * func_parser(func, y[n], x[n])
        y.append(round(y_next, 15))
    return y
