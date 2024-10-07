import numpy as np

def a(x):
    return np.sin(x) ** 2 + np.cos(x) ** 2

array = np.array([0,2,3,4,5])
print(a(array))