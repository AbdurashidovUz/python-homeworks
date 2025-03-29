#Normalize a 5x5 random matrix.
import numpy as np
x = np.random.random((5,5))
print(x)
xmax, xmin = x.max(), x.min()
x = (x - xmin)/(xmax - xmin)
print(x)

