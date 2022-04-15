from matplotlib import pyplot as plt
from numpy import arange

plt.plot(arange(0,100), linestyle="-.", color="#112021", lw=5, label="Graph")
plt.legend()
plt.show()