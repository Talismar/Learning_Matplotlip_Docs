from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,1,1000)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

plt.plot(x, y)

""" fill - Preenche """
# plt.fill(x, y, alpha=0.2)
plt.fill_between(x, y, alpha=0.2, where=(y >= 0), color="green")
plt.fill_between(x, y, alpha=0.2, where=(y < 0), color="red")
plt.show()