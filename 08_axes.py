from matplotlib import pyplot as plt
from numpy import arange

arr = arange(0,50)

plt.axes([0.06,0.06,0.9,0.8], facecolor="black", anchor='C')
plt.title(label="This is my label",fontdict={"color":"blue", "backgroundcolor":"#bababa"}, loc="center")
plt.plot(arr)
plt.show()