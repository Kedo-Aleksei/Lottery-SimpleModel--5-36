import matplotlib.pyplot as plt

value1 = [20, 30, 40]
value2 = [62, 5, 91, 25, 36, 32, 96, 95, 3, 90, 95, 32, 27, 55, 100, 15, 71, 11, 37, 21]
value3 = [23, 89, 12, 78, 72, 89, 25, 69, 68, 86, 19, 49, 15, 16, 16, 75, 65, 31, 25, 52]
value4 = [59, 73, 70, 16, 81, 61, 88, 98, 10, 87, 29, 72, 16, 23, 72, 88, 78, 99, 75, 30]

box_plot_data = [value1, value2, value3, value4]
plt.boxplot(box_plot_data, showbox=False)
plt.show()
