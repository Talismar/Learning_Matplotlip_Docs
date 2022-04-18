from matplotlib import pyplot as plt

class Graph:
  "My Graph"

  def __init__(self,):
        
    figure = plt.figure(figsize=(15,5), dpi=200)
    figure.suptitle("My title")

    figure.add_subplot(131)
    plt.title("Graph - Plot")
    plt.plot([1,2,3,4,5,6])

    figure.add_subplot(132)
    plt.title("Graph - Scatter")
    plt.scatter([1,2,3,4,5,6], [2,4,6,8,10,12])

    figure.add_subplot(133)
    plt.title("Graph - Bar", fontdict={'fontname':"Fira Code", "fontsize":20})
    plt.bar([1,2,3,4,5,6], [2,4,6,8,10,12], label="Talismar")
    plt.legend(loc=3, fontsize=10)

    plt.show()

Graph()