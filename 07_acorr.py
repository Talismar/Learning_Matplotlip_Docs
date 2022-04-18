from matplotlib import pyplot as plt
import numpy as np

arr = np.array([24.40, 10.25, 20.05, 22.00, 
                  61.90, 7.80, 15.00, 22.80,  
                  34.90, 57.30, 58.9])

plt.acorr(arr, maxlags=None)
plt.annotate(text="Talismar", xy=(5, 0.5),xytext=(1, 1),arrowprops=dict(arrowstyle="->"))

plt.show()