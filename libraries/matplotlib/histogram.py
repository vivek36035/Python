import matplotlib.pyplot as plt
data = [10, 20, 20, 30, 40, 40, 50, 60, 60, 70]
plt.hist(data, bins=5, color='purple')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()