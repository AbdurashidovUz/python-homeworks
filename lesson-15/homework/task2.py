import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x, sin_y, label='sin(x)', linestyle='-', marker='o', color='b')
plt.plot(x, cos_y, label='cos(x)', linestyle='--', marker='x', color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Plot')
plt.legend()
plt.grid(True)
plt.show()