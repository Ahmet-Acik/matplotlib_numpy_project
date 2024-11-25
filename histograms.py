import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Basic Histogram Example')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, density=True, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram with Density Plot Example')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.randn(1000)
data2 = np.random.randn(1000) + 2

plt.hist(data1, bins=30, alpha=0.5, label='Dataset 1')
plt.hist(data2, bins=30, alpha=0.5, label='Dataset 2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Multiple Datasets Example')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, cumulative=True, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Cumulative Frequency')
plt.title('Cumulative Histogram Example')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
bins = [-3, -2, -1, 0, 1, 2, 3]

plt.hist(data, bins=bins, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Custom Bin Sizes Example')
plt.show()