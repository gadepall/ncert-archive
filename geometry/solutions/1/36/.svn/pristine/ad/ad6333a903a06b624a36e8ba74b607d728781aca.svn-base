# Assignment 1
# Triangles
# Exercise 8.1, Problem 36 

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


# Creating Triangle ABC
a=6
b=4
c=5
A,B,C= tri_vert(a,b,c)
M= np.array([a/2,0])
# Creating triangle PQR
p=6
q=5
r=4
Q = np.array([8,0])
P=np.add(A,Q)
R=np.add(C,Q)
N=np.add(M,Q)

# Generating lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AM = line_gen(A,M) 
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)
x_PN = line_gen(P,N)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AM[0,:],x_AM[1,:],label='$AM$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_PN[0,:],x_PN[1,:],label='$PN$')



plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.08), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.03), M[1] * (1 - 0.1) , 'M')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.09), Q[1] * (1) , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1 + 0.03), N[1] * (1 - 0.1) , 'N')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
#plt.grid() # minor
plt.axis('equal')

plt.show()

