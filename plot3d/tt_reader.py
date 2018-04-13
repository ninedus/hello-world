"""
=============================================
Generate polygons to fill TT input
=============================================
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

import csv

qc_list = []

with open('tt_20180413.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['HOUR'], row['CRANE_NO'], row['TOTAL_TT'])
        qc_list.append({row['HOUR'], row['CRANE_NO'], row['TOTAL_TT']})

# rownum = 0
# with open('tt_20180413.csv', newline='') as csvfile:
#     line = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for data in line:
#         rownum += 1
#
#         if rownum == 1:
#             continue
#         print(', '.join(data))
#
#         item = ', '.split(data)
#         key = item[1] # QC
#         dict[key] = {dict[key], {item[1], item[0], item[3]}}


fig = plt.figure()
ax = fig.gca(projection='3d')

def cc(arg):
    return mcolors.to_rgba(arg, alpha=0.6)

xs = np.arange(0, 10, 0.4)
verts = []
zs = [0.0, 1.0, 2.0, 3.0]
for z in zs:
    ys = np.random.rand(len(xs))
    ys[0], ys[-1] = 0, 0
    verts.append(list(zip(xs, ys)))

poly = PolyCollection(verts, facecolors=[cc('r'), cc('g'), cc('b'),
                                         cc('y')])
poly.set_alpha(0.7)
ax.add_collection3d(poly, zs=zs, zdir='y')

ax.set_xlabel('QC')
ax.set_xlim3d(0, 10)
ax.set_ylabel('TT')
ax.set_ylim3d(0, 18)
ax.set_zlabel('HR')
ax.set_zlim3d(0, 1)

plt.show()
