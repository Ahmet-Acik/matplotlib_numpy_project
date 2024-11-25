import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph Example')
plt.legend()
plt.show()