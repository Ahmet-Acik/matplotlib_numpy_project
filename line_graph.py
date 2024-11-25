import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph Example')
plt.legend()
plt.show()



import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

plt.plot(x, y1, label='Line 1', color='blue')
plt.plot(x, y2, label='Line 2', color='red')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Multiple Lines Example')
plt.legend()
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', linestyle='-', color='green', label='Line with Markers')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph with Markers Example')
plt.legend()
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, linestyle='--', color='purple', label='Dashed Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Dashed Line Graph Example')
plt.legend()
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='Line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph with Annotations Example')
plt.annotate('Peak', xy=(5, 11), xytext=(4, 10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend()
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, label='Line', color='orange')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph with Grid Example')
plt.grid(True)
plt.legend()
plt.show()

