import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=False, patch_artist=True)
plt.xlabel('Value')
plt.ylabel('Category')
plt.title('Horizontal Box Plot Example')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
colors = ['pink', 'lightblue', 'lightgreen']

box = plt.boxplot(data, patch_artist=True)
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot with Custom Colors Example')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, notch=True, patch_artist=True)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot with Notches Example')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, showmeans=True, patch_artist=True)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot with Mean Line Example')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, whis=[5, 95], patch_artist=True)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Box Plot with Whiskers Example')
plt.show()

