#Code by GVV Sharma
#December 7, 2019
#released under GNU GPL
#Proof of Baudhyana Theorem

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Sides
a = 4
b = 3
c = np.sqrt(a**2+b**2)


#Triangle vertices
A = np.array([0,b]) 
B = np.array([a,0]) 
C = np.array([0,0]) 

#Mid point of A,B
M=np.array([a/2,b/2])
# Point D
D=np.array([a,b])


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_CM = line_gen(C,M)
x_MD = line_gen(M,D)
x_DB = line_gen(D,B)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CM[0,:],x_CM[1,:],label='$CM$')
plt.plot(x_MD[0,:],x_MD[1,:],label='$MD' )
plt.plot(x_DB[0,:],x_DB[1,:],label='$DB' )

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.05), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.05), C[1] * (1 - 0.1) , 'C')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.05), M[1] * (1 - 0.1) , 'M')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1), D[1] * (1 - 0.1) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()







