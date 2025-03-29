#Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
matrix = np.random.random((10, 10))
print(matrix)
print(matrix.min())
print(matrix.max())