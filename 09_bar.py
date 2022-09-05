from matplotlib import pyplot as plt

x = ["2018","2019","2020", "2021"]
y = [10,8,6,4]

# right edge pass a negative width
plt.bar(x, y, width=-0.1, align='edge')

# color of the bar
# plt.bar(x, y, width=0.5, align='center', color=['r', 'b'])

""" 
import matplotlib.pyplot as plt

def add_value_label(x_list, y_list):

    for i in range(1, len(x_list)+1):
        plt.text(i-0.18, y_list[i-1], y_list[i-1])

no_of_students = [10,24,45,30,23,56,67,34,45,50]
class_number = [1,2,3,4,5,6,7,8,9,10]

plt.bar(class_number,no_of_students)
add_value_label(class_number,no_of_students)
plt.title("No of Students in a class")
plt.xlabel("Class")
plt.ylabel("Number of Students")
"""
plt.show()