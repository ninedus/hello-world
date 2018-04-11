import numpy as np


a = np.linspace(1, 3, num=4)
print(a)

a = np.random.randn(1000)
h, b = np.histogram(a, bins=8, normed=True)
print(h)
print(b)

x = np.arange(100)
y = np.random.normal(4., 0.9, 100)
for i in range(100):
    y[i] = y[i] + i/40
a, b = np.polyfit(x, y, 1)
print(a, b)

#Reading and Writing Data to Files
a = np.arange(16).reshape(4,4)
print(a)

np.savetxt('data.txt', a, fmt="%G", delimiter=',')
b = np.loadtxt('data.txt', delimiter=',')
print(b)
