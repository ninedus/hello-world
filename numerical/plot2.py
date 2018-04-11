import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax = fig.add_subplot(3, 1, 1, polar=True)
x = np.arange(25)
y = np.sin(2 * np.pi * x / 25)
ax.bar(x * np.pi * 2/ 25, abs(y), width=0.3, alpha=0.3)

ax2 = fig.add_subplot(3, 1, 2)
x2 = np.arange(25)
y2 = np.sin(2 * np.pi * x2 / 25)
ax2.bar(x2, y2)

ax = fig.add_subplot(3, 1, 3)
x = np.arange(100)
y = np.sin(2 * np.pi * x / 100)
ax.plot(x, y, "g:")

plt.show()
