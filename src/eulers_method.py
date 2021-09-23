from function_parser import func_parser
import numpy as np

def eulers(func, a, b, y, N):
    '''
    Function apporximates y(x) using Eulers method along the interval [a,b].

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
        y_next = y[n] + h * func_parser(func, y[n], x[n])
        y.append(round(y_next, 15))
    return y
