from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60,40]
labels = ['Sixty', "Forty"]
colors = ["blue", "red"]

plt.pie(slices, labels=labels, colors=colors, explode=[0,0.5], autopct="%1.1f%%", wedgeprops={"edgecolor": "black"})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()