from matplotlib import pyplot as plt

x = ["2018","2019","2020", "2021"]
y = [10,8,6,4]

# right edge pass a negative width -> width=-0.1, align='edge'

plt.bar_label(container=plt.bar(x,y), labels=x, padding=3)
plt.show()
