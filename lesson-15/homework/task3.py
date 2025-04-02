import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

x = np.linspace(-10, 10, 400)

# Top-left: f(x) = x^3
axs[0, 0].plot(x, x**3, color='b')
axs[0, 0].set_title('f(x) = x^3')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')

# Top-right: f(x) = sin(x)
axs[0, 1].plot(x, np.sin(x), color='r')
axs[0, 1].set_title('f(x) = sin(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')

# Bottom-left: f(x) = e^x
axs[1, 0].plot(x, np.exp(x), color='g')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')

# Bottom-right: f(x) = log(x+1)
x_pos = np.linspace(0, 10, 400)
axs[1, 1].plot(x_pos, np.log(x_pos + 1), color='m')
axs[1, 1].set_title('f(x) = log(x+1)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

plt.tight_layout()
plt.show()