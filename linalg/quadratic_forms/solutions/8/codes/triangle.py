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
#a = 4
#b = 3
#c = np.sqrt(a**2+b**2)
a= 4.12
b= 4.47
c= 8.06


#Triangle vertices
#A = np.array([0,b]) 
#B = np.array([a,0]) 
#C = np.array([0,0]) 

A = np.array([4,-6]) 
#print(A)
B = np.array([3,-2]) 
C = np.array([5,2]) 


#Mid point of A,B
#M=np.array([a/2,b/2])
M= np.array((A+B)/2)
#print(M)
# Point D
#D=np.array([a,b])
#Mid point of B,C
N= np.array((C+B)/2)
#Mid point of C,A
P= np.array((C+A)/2)


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_CM = line_gen(C,M)
x_BP = line_gen(B,P)
x_AN = line_gen(A,N)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CM[0,:],x_CM[1,:],label='$CM$')
plt.plot(x_BP[0,:],x_BP[1,:],label='$BP$' )
plt.plot(x_AN[0,:],x_AN[1,:],label='$AN$' )

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.05), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.05), C[1] * (1 - 0.1) , 'C')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.05), M[1] * (1 - 0.1) , 'M')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1), N[1] * (1 - 0.1) , 'N')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1), P[1] * (1 - 0.1) , 'P')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()

