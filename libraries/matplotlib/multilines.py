import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [15, 18, 22, 27, 35]
plt.plot(x, y1, label='Set 1')
plt.plot(x, y2, label='Set 2')
plt.title("Multiple Line Graphs")
plt.legend()
plt.show()