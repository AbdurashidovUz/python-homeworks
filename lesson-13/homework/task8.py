#Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).

import numpy as np
x = np.random.random((5,3))
y = np.random.random((3,2))
print(x)
print(y)
print(np.dot(x, y))
