import numpy as np

def power(base, exp):
    return base ** exp

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power)
results = vectorized_power(bases, exponents)

print(results)