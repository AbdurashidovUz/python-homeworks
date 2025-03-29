#Solve the linear system ( Ax = b ) where ( A ) is a 3x3 matrix, and ( b ) is a 3x1 column vector.

import numpy as np
A = np.random.random((3,3))
b = np.random.random((3,1))
print(A)
print(b)
x = np.linalg.solve(A, b)
print(x)