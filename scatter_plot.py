import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', alpha=0.5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot Example')
plt.show()