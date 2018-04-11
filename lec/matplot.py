import numpy as np
import matplotlib.pyplot as py

x = np.arange(-3, 3, 0.1)

y = x**2 - x - 2

py.plot(x, y)

py.show()
