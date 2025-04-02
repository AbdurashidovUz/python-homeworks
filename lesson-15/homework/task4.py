import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, c='b', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of 100 Random Points')
plt.grid(True)
plt.show()