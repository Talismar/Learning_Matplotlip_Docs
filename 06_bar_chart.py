from matplotlib import pyplot as plt
from numpy import arange

x = arange(0,5)
y = arange(0,5)

bars = plt.bar(x, y)

bars[2].set_hatch("/")
bars[3].set_hatch("O")
bars[4].set_hatch("*")


plt.show()