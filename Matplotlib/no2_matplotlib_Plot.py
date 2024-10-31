from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")  # 'ggplot' is one type of style in matplotlib

x1 = [1, 2, 3, 4, 5]
y1 = [10, 2, 8, 3, 5]
x2 = [1, 2, 3, 4, 5]
y2 = [3, 4, 5, 6, 7]
plt.plot(x1, y1, label="first", linewidth=5)
plt.plot(x2, y2, label="second")
plt.legend()  # to show label in your chart
plt.show()
