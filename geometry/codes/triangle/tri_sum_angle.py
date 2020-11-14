#Code by GVV Sharma
#December 6, 2019
#released under GNU GPL
#Drawing a right angled triangle

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Sides
a = 4
c = 3

#Section Ratio
k = 0.2

#Triangle vertices
A = np.array([0,c]) 
B = np.array([0,0]) 
C = np.array([a,0]) 

#Translating coordinates
Y = A + np.array([1,0]) 
X = A - np.array([1,0]) 
T = A + np.array([0,1]) 
V = (k+1)*A - k*C

#Generating all lines
x_XY = line_gen(X,Y)
x_BT = line_gen(B,T)
x_CV = line_gen(C,V)
x_BC = line_gen(C,B)

#Plotting all lines
plt.plot(x_XY[0,:],x_XY[1,:],label='$XY$')
plt.plot(x_BT[0,:],x_BT[1,:],label='$BT$')
plt.plot(x_CV[0,:],x_CV[1,:],label='$CV$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(X[0], X[1], 'o')
plt.text(X[0] * (1 + 0.03), X[1] * (1 - 0.1) , 'X')
plt.plot(Y[0], Y[1], 'o')
plt.text(Y[0] * (1 + 0.03), Y[1] * (1 - 0.1) , 'Y')
plt.plot(T[0], T[1], 'o')
plt.text(T[0] * (1 + 0.03), T[1] * (1 - 0.1) , 'T')
plt.plot(V[0], V[1], 'o')
plt.text(V[0] * (1 + 0.03), V[1] * (1 - 0.1) , 'V')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('./figs/triangle/tri_sum_angle.pdf')
plt.savefig('./figs/triangle/tri_sum_angle.eps')
subprocess.run(shlex.split("termux-open ./figs/triangle/tri_sum_angle.pdf"))
#else
#plt.show()







