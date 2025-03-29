#Create two matrices ( A ) (3x4) and ( B ) (4x3), and compute the matrix product ( A \cdot B ).
import numpy as np
A = np.random.random((3,4))
B = np.random.random((4,3))
print(A)
print(B)
print(np.dot(A, B))
