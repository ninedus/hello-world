from scipy import optimize

#import cvxopt

import matplotlib.pyplot as plt
import matplotlib

import numpy as np

import sympy

'''
sympy.init_printing()

r, h = sympy.symbols("r, h")
Area = 2 * sympy.pi * r**2 + 2 * sympy.pi * r * h
Volume = sympy.pi * r**2 * h
h_r = sympy.solve(Volume - 1)[0]
Area_r = Area.subs(h_r)
rsol = sympy.solve(Area_r.diff(r))[0]
print(rsol)

#_.evalf()
Area_r.diff(r, 2).subs(r, rsol)
Area_r.subs(r, rsol)
def f(r):
    return 2 * np.pi * r**2 + 2 / r

r_min = optimize.brent(f, brack=(0.1, 4))
print(r_min)

print(f(r_min))

a1 = np.array([1, 4, 5, 7, 9])

print("a1.mean()=", a1.mean())
print("a1.std()=", a1.std())
print("a1.var()=", a1.var())

a = np.arange(16)
a2 = a.reshape(2, 8)
a4 = a.reshape(4, 4)
print("a2=", a2)
print("a4=", a4)
'''

print("matplotlib: ", matplotlib.__version__)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.arange(100)
y = np.sin(2 * np.pi * x / 100)
ax.plot(y)
#ax.plot(x, y, "g:")
#ax.plot(x, y, linestyle='dashed', color='blue')

plt.show()
