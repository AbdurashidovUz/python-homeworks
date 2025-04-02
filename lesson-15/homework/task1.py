import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x^2 - 4x + 4')
plt.grid(True)
plt.show()