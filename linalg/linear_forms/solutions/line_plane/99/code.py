# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 04:35:25 2020

@author: N Praful Raj
"""


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')


#the quation of plane is r.n=d
#here r is defined by the point variable
#n is defined by normal varible

point  = np.array([1,-2,7])
normal = np.array([2,1,1])
d = -point.dot(normal)

xx, yy = np.meshgrid(np.arange(1,11),np.arange(1,11))


z = ((-normal[0] * xx - normal[1] * yy -d) * 1. / normal[2])

ax.plot_surface(xx, yy, z)
#5*ax.plot_surface(xx, yy, z)
ax.plot3D([1],[-2],[7],marker='o',label='[1,-2,7]')
ax.plot3D([3],[-4],[-5],marker='o',label='[3,4,5]')
ax.plot3D([2],[-3],[1],marker='o',label='[2,3,1')
ax.plot([3,2],[-4,-3],[-5,1], label='line')
ax.legend()

plt.xlabel('X')
plt.ylabel('Y')
plt.zlabel('Z')

plt.show()
