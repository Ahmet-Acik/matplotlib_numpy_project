import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]

plt.bar(categories, values, color='green', alpha=0.7)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()



import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]

plt.barh(categories, values, color='blue', alpha=0.7)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart Example')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
values1 = [3, 7, 5, 4]
values2 = [2, 6, 4, 3]

bar_width = 0.35
index = np.arange(len(categories))

plt.bar(index, values1, bar_width, label='Group 1', color='blue', alpha=0.7)
plt.bar(index + bar_width, values2, bar_width, label='Group 2', color='green', alpha=0.7)

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Chart Example')
plt.xticks(index + bar_width / 2, categories)
plt.legend()
plt.show()


import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values1 = [3, 7, 5, 4]
values2 = [2, 6, 4, 3]

plt.bar(categories, values1, label='Group 1', color='blue', alpha=0.7)
plt.bar(categories, values2, bottom=values1, label='Group 2', color='green', alpha=0.7)

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart Example')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]
errors = [0.5, 1.0, 0.7, 0.3]

plt.bar(categories, values, yerr=errors, color='purple', alpha=0.7, capsize=5)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Error Bars Example')
plt.show()

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]
colors = ['red', 'blue', 'green', 'orange']

plt.bar(categories, values, color=colors, alpha=0.7)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Custom Colors Example')
plt.show()