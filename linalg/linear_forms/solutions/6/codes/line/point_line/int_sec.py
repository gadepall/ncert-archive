import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

A = np.array([-2,-2])
B = np.array([2,-4])
P = np.array([-2/7,-20/7])

x_AB = line_gen(A,B)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1.05), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0]-0.1, B[1]+0.2 , 'B')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.05) , 'P')

plt.title('Line $AB$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()