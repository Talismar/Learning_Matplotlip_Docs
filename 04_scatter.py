from matplotlib import pyplot as plt

plt.scatter([1,2,3,4,5,6,7,8,9,10], [2,4,6,8,10,12,14,16,18,20], marker="s", color="#806040", label="Graph" )
plt.legend()
plt.axis(xmin=-1, xmax=20, ymin=-5, ymax=25)
plt.grid()
plt.show()