from matplotlib import pyplot as plt

x = ["2018","2019","2020", "2021"]
y = [10,8,6,4]

aux = -1
def autop():
  global aux
  aux+=1
  return str(y[aux])


""" plt.pie(y, labels=x, shadow=True, rotatelabels=False, autopct=lambda x: autop()) """
patches = plt.pie(y, autopct="%1.2f%%", shadow=True, startangle=140)

plt.legend(x, loc="best",bbox_to_anchor=(0, 0.5, 0.2, 0.),fontsize="xx-large", labelcolor="green", title="My legend")
plt.show()