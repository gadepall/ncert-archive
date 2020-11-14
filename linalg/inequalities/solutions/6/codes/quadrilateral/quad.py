import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

A = np.array([-4,2])
B = np.array([-3,-5])
C = np.array([3,-2])
D = np.array([2,3])

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0]-0.3, B[1]-0.3 , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1.05),D[1]+0.1,'D')

plt.title('Quadrilateral $ABCD$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()