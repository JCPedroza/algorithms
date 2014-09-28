import math
import numpy as np

pi = np.pi

def frac(x):
    """ Returns the fractional part of x """
    return x - math.floor(x)

def csc(x):
    """ Cosecant function """
    sin = np.sin(x)
    if sin != 0:
        return 1.0/sin
    else:
        return 0

def sin(x):
    return np.sin(x)

def arcsin(x):
    return np.arcsin(x)

def floor(x):
    return math.floor(x)

