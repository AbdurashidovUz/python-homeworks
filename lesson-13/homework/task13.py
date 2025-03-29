#Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.

import numpy as np
x = np.random.random((3,3))
y = np.random.random((3,1))
print(x)
print(y)
print(np.dot(x, y))
