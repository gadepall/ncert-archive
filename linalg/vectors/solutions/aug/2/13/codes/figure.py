#Code by GVV Sharma
#November 19, 2019
#released under GNU GPL
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from coeffs import *

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Points on the plane
A = np.array([1,-2,-8]).reshape((3,1))
B = np.array([5,0,-2]).reshape((3,1))
C = np.array([11,3,7]).reshape((3,1))

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")
plt.plot(x_CA[0,:],x_CA[1,:],x_CA[2,:],label="CA")

#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.text(1,-2,-8, "A", color='red')
ax.text(5,0,-2, "B", color='red')
ax.text(11,3,7, "C", color='red')

#save plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.savefig('../figures/figure.png')
