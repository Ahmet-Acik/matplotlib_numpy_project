import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.rand(50) * 100
y_data = np.random.rand(50) * 100

plt.scatter(x_data, y_data, c="blue", alpha=0.5, marker='*', label="scatter point")
plt.show()

years =[2006 + i for i in range(18)]
weights = [0.5, 0.6, 0.8, 1.4, 1.6, 1.8, 2.0, 2.2, 1.0, 1.2, 2.4, 3.0, 3.2, 3.4,  2.6, 2.8,3.6, 3.8]

plt.plot(years, weights, color='b', marker='o', linestyle='--', linewidth=3, markersize=6)
plt.show()

x_pro =["C++", "Java", "Python", "JavaScript", "C#", "PHP"]
y_pro =[20, 30, 25, 10, 15, 10]

plt.bar(x_pro, y_pro, color='b', alpha=0.5)
plt.show() 