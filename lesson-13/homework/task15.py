#Given a 5x5 matrix, find the row-wise and column-wise sums.
import numpy as np
x = np.random.random((5,5))
print(x)
print(x.sum(axis=1))
print(x.sum(axis=0))
