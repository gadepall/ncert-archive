import matplotlib.pyplot as plt 
import numpy as np 
from coeffs import *
import subprocess
import shlex

A = np.array([2,-5])
B = np.array([-7,0])
C = np.array([-2,9])

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')

plt.plot(A[0],A[1],'o')
plt.text(2.2 , -5.1, 'A')
plt.plot(B[0] ,B[1] , 'o')
plt.text(-7.5, 0 , 'B')
plt.plot(C[0],C[1],'o')
plt.text(-2.2, 9.2 , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()