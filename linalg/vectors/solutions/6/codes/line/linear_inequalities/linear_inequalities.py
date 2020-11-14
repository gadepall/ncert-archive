import matplotlib.pyplot as plt 
import numpy as np 
from coeffs import *
import subprocess
import shlex

A = np.array([-4,9])
B = np.array([6,-6])
C = np.array([10,9])
D = np.array([10,-6])
points = np.array((A,C,D,B))

x_AB = line_gen(A,B)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(2, 0, 'o')
plt.text(2 , -1, 'A')
plt.plot(0 ,3 , 'o')
plt.text(0, 2 , 'B')
plt.fill(points[:,0], points[:,1], 'k', alpha=0.7)

plt.title('Solution of $3x+2y>6$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()