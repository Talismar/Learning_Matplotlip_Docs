from matplotlib import animation, pyplot as plt
import numpy as np

x = np.arange(1,50)
y = np.arange(10,99+9, 2)
""" 
plt.plot(x, y, label="Talismar",
               linestyle='dashed',
               linewidth=2,
               color="black",
               marker="o",
               markersize=1
                ) 
plt.show()
"""

plt.plot(x, y, 'ro-', linewidth=2, markersize=5)
plt.show()


""" Plotting labelled data """
""" 
data = {"x":x,"y":y}
plt.plot("x", "y", data=data)
plt.show()
"""

""" 
plt.plot(x, y)
plt.plot(x1, y1, 'g--', x2, y2, 'g-')
"""
""" 
x1 = [1, 2, 3]
y1 = np.array([[2, 3], [4, 5], [6, 7]])
x2 = [3, 4, 6]
y2 = np.array([[4, 2], [3, 4], [5, 6]])
plt.plot(x1, y1, label=["Plot - X1","Plot - Y1"])
plt.plot(x2, y2, label=["Plot - X2","Plot - Y2"], animation=True)
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.xticks([i for i in range(0,10,2)])
plt.yticks([i for i in range(0,10,1)])
plt.legend()
plt.title("Here is the title")
plt.show() """