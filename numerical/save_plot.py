import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.arange(100)
y = np.sin(2 * np.pi * x / 100)
ax.plot(y)
plt.savefig('sin-wave.png')
plt.savefig('sin-wave.pdf')
