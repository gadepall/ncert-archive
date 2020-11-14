import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#2 Points
A = np.array([3,4]) 
B = np.array([-1,2])

#Midpoint 
Mid = np.array([1,3])
 
n = np.array([2,1])
m = omat@n
k1=0
k2=2

#Generate all lines
x_AB = line_gen(A,B)
x_perp_bisect = line_dir_pt(m,Mid,k1,k2)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_perp_bisect[0,:],x_perp_bisect[1,:],label='$Right Bisector$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.1), B[1] * (1-0.1) , 'B')
plt.plot(Mid[0], Mid[1], 'o')
plt.text(Mid[0] * (1 - 0.2), Mid[1] * (1+0.1) , 'Mid')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('square')

plt.savefig('Figure1.png')

plt.show()
