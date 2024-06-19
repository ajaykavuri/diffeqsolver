import numpy
from math import exp, sin, cos, pi, log, sqrt, atan, atan2, tan, asin
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import pandas as pd

def diffeq(x, y):
    return exp(-1*sin(x))

def solvenext(x0, y0, dx):
    """
    Returns y1 (i.e. next value) in function
    """
    dydx = diffeq(x0, y0)
    return y0 + dydx*(dx)

def solveprev(x0, y0, dx):
    """
    Returns ysub(-1) (i.e. previous value) in function
    """
    dydx = diffeq(x0, y0)
    return y0 - dydx*(dx)

def generate_coords(init_coords: tuple, dx) -> tuple:
    x_coords = []
    y_coords = []
    x_coords.append(init_coords[0])
    y_coords.append(init_coords[1])
    x = init_coords[0]
    y = init_coords[1]
    for i in range(10000):
        y = solveprev(x, y, dx)
        x -= dx
        x_coords.append(x)
        y_coords.append(y)
    x = init_coords[0]
    y = init_coords[1]
    for i in range(10000):
        y = solvenext(x, y, dx)
        x += dx
        x_coords.append(x)
        y_coords.append(y)
    return x_coords, y_coords

coords = pd.DataFrame(generate_coords((0, 1), 0.01))
coords = coords.transpose()
print(coords.head())
plt.plot(coords[0], coords[1])
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.show()